# 🚀 CoinMarketCap ETL Pipeline with Apache Airflow

This project is an **ETL (Extract, Transform, Load)** pipeline built using **Apache Airflow** to fetch cryptocurrency data from the CoinMarketCap API, transform it, and load it into a MySQL database. 💰📊

---

## 🔍 Project Overview

The pipeline performs the following tasks on a **daily schedule**:

* 🛠️ **Extract:** Retrieve the latest cryptocurrency listings from the CoinMarketCap API and save raw JSON data locally.
* 🔄 **Transform:** Process and normalize the JSON data into a clean pandas DataFrame, format key fields, and save it as JSON.
* 💾 **Load:** Insert the transformed data into the MySQL database table `crypto_prices`.

---

## 🛠️ Technologies Used

* 🐍 Python 3.x
* ✈️ Apache Airflow
* 🔗 Requests (HTTP API calls)
* 🐼 pandas (Data processing)
* 🐬 MySQL Connector/Python (Database interaction)
* 🗄️ MySQL Database

---

## ⚙️ Setup & Installation

1. **Clone the repository**

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create and activate a Python virtual environment (optional but recommended)**

   * Linux/Mac:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Set your MySQL credentials securely:

   ```bash
   export MYSQL_USER=<your_mysql_username>
   export MYSQL_PASSWORD=<your_mysql_password>
   ```

   *(Adjust for your OS and shell)*

5. **Set up MySQL Database**
   Create the database and table:

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
   Place the DAG file in Airflow’s DAGs folder and start scheduler & webserver.

---

## 🚀 Usage

* Start Airflow scheduler and webserver:

  ```bash
  airflow scheduler
  airflow webserver
  ```

* Open the Airflow UI at [http://localhost:8080](http://localhost:8080) in your browser.

* Trigger the DAG named `mainDAG` manually or wait for the daily scheduled runs.

---

## 📝 Notes

* 🔐 **Important:** Replace the hardcoded CoinMarketCap API key with your own or load it from environment variables securely.
* 📂 Ensure the `./data` directory exists or update file paths accordingly.
* ⏳ Airflow retry attempts and delays are configured in the DAG `default_args`.
* ⚠️ Error handling is implemented for API requests and database operations for robustness.

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 📬 Contact

Created by **Shishir Raj Giri**
Feel free to reach out at \[[shishirgiri81@gmail.com](mailto:shishirgiri81@gmail.com)] for any questions or feedback!