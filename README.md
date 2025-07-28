Sure! Here’s the README.md content ready for you to copy and paste directly:

````markdown
# 🚀 CoinMarketCap Data Pipeline using Apache Airflow

---

## 🔍 Project Overview

This project builds an automated **ETL pipeline** that fetches cryptocurrency data from the CoinMarketCap API, processes it, and loads it into a MySQL database — all orchestrated by **Apache Airflow**!

---

## ✨ Features

- 🔄 **Extract**: Fetches latest data for up to 5000 cryptocurrencies from CoinMarketCap API  
- 🔧 **Transform**: Cleans and normalizes data, selecting key fields and formatting timestamps  
- 💾 **Load**: Inserts processed data into a MySQL table `crypto_prices`  
- ⏰ **Automation**: Runs daily using Airflow's DAG scheduler  
- ⚙️ **Resilience**: Retries on failure with exponential backoff  

---

## 🛠️ Technologies Used

| Technology          | Purpose                      |
|---------------------|------------------------------|
| 🐍 Python 3.x       | Pipeline scripting            |
| 🐝 Apache Airflow   | Workflow orchestration        |
| 📊 pandas           | Data manipulation             |
| 🌐 requests         | API calls                    |
| 🐬 MySQL            | Data storage                 |
| 🗄️ mysql-connector-python | MySQL connection from Python |
| 🔑 CoinMarketCap API | Cryptocurrency data source   |

---

## 📋 Prerequisites

- MySQL Server installed & running  
- Airflow installed and configured  
- Valid CoinMarketCap API key  
- Python environment with required packages  

---

## ⚙️ Setup & Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/shishirgiri81/CoinMarketCap-Data-Pipeline-Using-Airflow.git
   cd CoinMarketCap-Data-Pipeline-Using-Airflow
````

2. **Create & activate Python virtual environment**

   ```bash
   python3 -m venv py_env
   source py_env/bin/activate
   pip install -r requirements.txt
   ```

3. **Set MySQL credentials as environment variables**

   ```bash
   export MYSQL_USER='your_mysql_username'
   export MYSQL_PASSWORD='your_mysql_password'
   ```

4. **Create MySQL table**
   Run this in your MySQL client:

   ```sql
   CREATE TABLE crypto_prices (
       id INT PRIMARY KEY,
       name VARCHAR(255),
       symbol VARCHAR(50),
       slug VARCHAR(255),
       date_added DATETIME,
       max_supply BIGINT,
       circulating_supply BIGINT,
       total_supply BIGINT,
       cmc_rank INT,
       last_updated DATETIME,
       price FLOAT,
       volume_24h FLOAT,
       volume_change_24h FLOAT,
       percent_change_1h FLOAT,
       percent_change_24h FLOAT,
       percent_change_7d FLOAT,
       percent_change_30d FLOAT,
       percent_change_60d FLOAT,
       percent_change_90d FLOAT,
       market_cap FLOAT,
       market_cap_dominance FLOAT
   );
   ```

5. **Initialize & start Airflow**

   ```bash
   airflow db init
   airflow webserver --port 8080
   airflow scheduler
   ```

6. **Deploy DAG file**
   Place your DAG `.py` file inside Airflow’s `dags/` directory.

---

## ▶️ Running the Pipeline

* The DAG **`mainDAG`** runs automatically every day (`@daily`)
* You can also manually trigger runs via the Airflow UI or CLI

---

## ⚠️ Notes

* Replace the API key in the extract function with your own valid CoinMarketCap API key! 🔑
* Intermediate JSON data is stored under the `./data/` folder
* API and database exceptions are handled gracefully with retries and logging

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use and modify! 💡

---

*Made with ❤️ by Shishir Raj Giri*

```

Just paste it in your `README.md` file! Let me know if you want it customized more.
```
