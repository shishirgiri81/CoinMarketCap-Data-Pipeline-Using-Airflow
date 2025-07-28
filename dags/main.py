from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
import mysql.connector



from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


# Extract function to fetch the data from CoinMarketCap API and save it as a JSON file
def extract():

  # Define the path where the data will be saved
  file_path = './data/crypto_data.json'


  # Define the API URL and parameters to get the cryptocurrency data
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  
  parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
  }

  # API headers with the API key for authentication
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '3f5fafec-94cf-41a1-8276-ca034aba727a',
  }


  # Create a session to handle the request
  session = Session()
  session.headers.update(headers)

  try:
    # Send a GET request to fetch the data
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    # Write the JSON data to a file
    with open(file_path, 'w') as f:
      json.dump(data,f)
  
    # Return the file path for the next task
    return file_path
    

  # Handle different types of errors that might occur during the request
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
    return None



# Transform function to process the extracted data and format it into a DataFrame
def transform(ti):

  # Pull the file path from the 'extract' task using XCom
  file_path = ti.xcom_pull(task_ids = 'extract')
  
  # Read the saved JSON data from the file
  with open(file_path, 'r') as f:
    data = json.load(f)

  # data = pd.read_json(file_path, orient='records', lines=True)


  # Normalize the nested data to create a flat structure
  coins = data['data']


  # Convert the list of coins into a pandas DataFrame
  data = pd.DataFrame.from_dict(pd.json_normalize(coins), orient = 'columns')


  # Select only the required columns
  data = data[['id', 'name', 'symbol', 'slug', 'date_added',
       'max_supply', 'circulating_supply', 'total_supply', 'cmc_rank',
        'last_updated', 'quote.USD.price', 'quote.USD.volume_24h',
       'quote.USD.volume_change_24h', 'quote.USD.percent_change_1h',
       'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d',
       'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d',
       'quote.USD.percent_change_90d', 'quote.USD.market_cap',
       'quote.USD.market_cap_dominance']]


  # Fill any missing 'max_supply' values with 0
  data['max_supply'] =data['max_supply'].fillna(0)

  # Convert 'last_updated' column to datetime format
  data['last_updated'] = pd.to_datetime(data['last_updated']).dt.strftime('%Y-%m-%d %H:%M:%S')



  data['date_added'] = pd.to_datetime(data['date_added']).dt.strftime('%Y-%m-%d %H:%M:%S')



  # Convert 'total_supply' column to numeric type
  data['total_supply'] = pd.to_numeric(data['total_supply'])

  # Convert the DataFrame to a JSON object
  # data = data.to_json(file_path, orient='records', lines=True)

  # data.to_json(file_path, orient='records', lines=True)

  data = data.to_json()



  # Save the processed data back to the JSON file
  with open(file_path, 'w') as f:
    json.dump(data,f)
    
  # Return the file path for the next task or for future use
  return file_path





def load(ti):

  file_path = ti.xcom_pull(task_ids = 'transform')

  # with open(file_path, 'r') as f:
  #   data = json.load(f)
  
  # df = pd.read_json(data)

  # df = pd.read_json(file_path, orient='records', lines=True)

  # Read the saved JSON data from the file
  with open(file_path, 'r') as f:
    data = json.load(f)

  data = pd.read_json(data)

  # # Normalize the nested data to create a flat structure
  # coins = data['data']


  # # Convert the list of coins into a pandas DataFrame
  # data = pd.DataFrame.from_dict(pd.json_normalize(coins), orient = 'columns')

  # df = pd.read_json(file_path, orient='records', lines=True)

  print(f"Data shape before insert: {data.shape}")
  print(f"Data preview:\n{data.head()}")




  try:
    conn = mysql.connector.connect(
        host='localhost',
        user=os.getenv('MYSQL_USER'),        # MySQL username from env var
        password=os.getenv('MYSQL_PASSWORD'),# MySQL password from env var
        database='cmc_db'                    # Your database name
    )
  
    cursor = conn.cursor()

    insert_query = """
      INSERT INTO crypto_prices (
          id, name, symbol, slug, date_added, max_supply, circulating_supply, total_supply,
          cmc_rank, last_updated, price, volume_24h, volume_change_24h, percent_change_1h,
          percent_change_24h, percent_change_7d, percent_change_30d, percent_change_60d,
          percent_change_90d, market_cap, market_cap_dominance
      ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
      
    for row in data.itertuples(index = False):
      cursor.execute(insert_query, tuple(row))

    conn.commit()
  
  except mysql.connector.Error as err:

    print(f"Database error: {err}")
    
  finally:
      if cursor:
          cursor.close()
      if conn:
          conn.close()

  # conn = mysql.connector.connect(
  #       host='localhost',
  #       user=os.getenv('MYSQL_USER'),        # MySQL username from env var
  #       password=os.getenv('MYSQL_PASSWORD'),# MySQL password from env var
  #       database='cmc_db'                    # Your database name
  #   )
  
  # cursor = conn.cursor()

  # insert_query = """
  #   INSERT INTO crypto_prices (
  #       id, name, symbol, slug, date_added, max_supply, circulating_supply, total_supply,
  #       cmc_rank, last_updated, price, volume_24h, volume_change_24h, percent_change_1h,
  #       percent_change_24h, percent_change_7d, percent_change_30d, percent_change_60d,
  #       percent_change_90d, market_cap, market_cap_dominance
  #   ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
  #   """
    
  # for row in df.itertuples(index = False):
  #   cursor.execute(insert_query, tuple(row))

  # conn.commit()
  # cursor.close()
  # conn.close()



  





with DAG(

  default_args = {
    'owner': 'Shishir',
    'retries': 5,
    'retry_delay': timedelta(minutes = 2)
  },

  dag_id = 'mainDAG',
  description = 'CoinMarketCap',
  start_date = datetime(2025, 7, 26),
  schedule_interval = '@daily'

) as dag:

  task1 = PythonOperator(
    task_id = 'extract',
    python_callable = extract
  )

  task2 = PythonOperator(
    task_id = 'transform',
    python_callable = transform
  )

  task3 = PythonOperator(
    task_id = 'load',
    python_callable = load
  )



  task1 >> task2 >> task3