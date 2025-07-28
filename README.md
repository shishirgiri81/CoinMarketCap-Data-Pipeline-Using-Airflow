# CoinMarketCap ETL Pipeline with Apache Airflow

This project is an ETL (Extract, Transform, Load) pipeline built using Apache Airflow to fetch cryptocurrency data from the CoinMarketCap API, transform it, and load it into a MySQL database.

---

## Project Overview

The pipeline performs the following tasks on a daily schedule:

* **Extract:** Retrieves the latest cryptocurrency listings from the CoinMarketCap API and saves the raw JSON data locally.
* **Transform:** Processes and normalizes the extracted JSON data into a structured pandas DataFrame, cleans and formats key fields, then saves it back as JSON.
* **Load:** Reads the transformed data and inserts it into a MySQL database table named `crypto_prices`.

---

## Technologies Used

* Python 3.x
* Apache Airflow
* Requests library for HTTP API calls
* pandas for data processing
* MySQL Connector/Python for database interaction
* MySQL Database

---

## Setup & Installation

1. **Clone the repository**
   `git clone <repository_url>`
   `cd <repository_folder>`

2. **Create and activate a Python virtual environment (optional but recommended)**
   On Linux/Mac:
   `python3 -m venv venv`
   `source venv/bin/activate`
   On Windows:
   `python -m venv venv`
   `venv\Scripts\activate`

3. **Install required packages**
   `pip install -r requirements.txt`

4. **Configure Environment Variables**
   Set your MySQL credentials as environment variables:

   ```bash
   export MYSQL_USER=<your_mysql_username>
   export MYSQL_PASSWORD=<your_mysql_password>
   ```

   (Adjust according to your OS/shell)

5. **Set up MySQL Database**
   Create the database and table with this example schema:

   ```sql
   CREATE DATABASE cmc_db;

   USE cmc_db;

   CREATE TABLE crypto_prices (
       id INT PRIMARY KEY,
       name VARCHAR(100),
       symbol VARCHAR(50),
       slug VARCHAR(100),
       date_added DATETIME,
       max_supply BIGINT,
       circulating_supply BIGINT,
       total_supply BIGINT,
       cmc_rank INT,
       last_updated DATETIME,
       price DECIMAL(20,8),
       volume_24h BIGINT,
       volume_change_24h FLOAT,
       percent_change_1h FLOAT,
       percent_change_24h FLOAT,
       percent_change_7d FLOAT,
       percent_change_30d FLOAT,
       percent_change_60d FLOAT,
       percent_change_90d FLOAT,
       market_cap BIGINT,
       market_cap_dominance FLOAT
   );
   ```

6. **Configure Airflow**
   Place your DAG file in the Airflow DAGs directory and start the scheduler and webserver.

---

## Usage

* Start Airflow scheduler and webserver:
  `airflow scheduler`
  `airflow webserver`

* Open Airflow UI at `http://localhost:8080` in your browser.

* Trigger the DAG named `mainDAG` manually or wait for the daily scheduled run.

---

## Notes

* Replace the hardcoded CoinMarketCap API key with your own or store it securely as an environment variable.
* Ensure the `./data` directory exists or adjust the file paths accordingly.
* Airflow task retries and delays are configured in the DAG's `default_args`.
* Proper error handling is implemented for API requests and database operations.

---

## License

This project is open source under the [MIT License](LICENSE).

---

## Contact

Created by Shishir Raj Giri
Feel free to contact me at \[[shishirgiri81@gmail.com](mailto:shishirgirir81@gmal.com)] for questions or feedback.

