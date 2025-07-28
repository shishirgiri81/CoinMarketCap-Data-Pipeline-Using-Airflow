Sure! Here’s a clean, professional, and well-structured README content for your Airflow ETL pipeline project that you can directly use:

````markdown
# CoinMarketCap ETL Pipeline with Apache Airflow

This project is an ETL (Extract, Transform, Load) pipeline built using Apache Airflow to fetch cryptocurrency data from the CoinMarketCap API, transform it, and load it into a MySQL database.

---

## Project Overview

The pipeline performs the following tasks on a daily schedule:

- **Extract:** Retrieves the latest cryptocurrency listings from the CoinMarketCap API and saves the raw JSON data locally.
- **Transform:** Processes and normalizes the extracted JSON data into a structured pandas DataFrame, cleans and formats key fields, then saves it back as JSON.
- **Load:** Reads the transformed data and inserts it into a MySQL database table named `crypto_prices`.

---

## Technologies Used

- Python 3.x
- Apache Airflow
- Requests library for HTTP API calls
- pandas for data processing
- MySQL Connector/Python for database interaction
- MySQL Database

---

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
````

2. **Create and activate a Python virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Set the following environment variables for MySQL connection:

   ```bash
   export MYSQL_USER=<your_mysql_username>
   export MYSQL_PASSWORD=<your_mysql_password>
   ```

5. **Set up MySQL Database**

   Create the database and the `crypto_prices` table. Example schema:

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

   Make sure your Airflow environment is set up and the DAG file is placed in the Airflow DAGs folder.

---

## Usage

* Start your Airflow scheduler and webserver:

  ```bash
  airflow scheduler
  airflow webserver
  ```

* Access the Airflow UI (usually at `http://localhost:8080`).

* Trigger the `mainDAG` DAG manually or wait for the scheduled run (`@daily`).

---

## Code Summary

* `extract`: Fetches data from CoinMarketCap API and saves raw JSON.
* `transform`: Reads JSON, normalizes, cleans, and converts it to structured data.
* `load`: Inserts the transformed data into MySQL database.

---

## Notes

* API Key for CoinMarketCap is hardcoded in the `extract` function — **replace it with your own API key** or load it securely via environment variables.
* Make sure the `./data` directory exists or adjust the path accordingly.
* Error handling is implemented during API requests and MySQL interactions.
* Retries and retry delays are configured for Airflow tasks.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Contact

Created by Shishir Raj Giri
For any questions or feedback, please reach out at \[[your-email@example.com](mailto:your-email@example.com)].

```

If you want, I can also help you generate a `requirements.txt` or Dockerfile for this setup! Let me know.
```
