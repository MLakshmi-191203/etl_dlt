# 🚀 CSV to PostgreSQL ETL Pipeline using dlt

## 📌 Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python and dlt.

The pipeline extracts data from a CSV file, performs basic transformations, and loads it into PostgreSQL.

---

## 🛠️ Tech Stack

* Python
* dlt (Data Load Tool)
* PostgreSQL
* Pandas

---

## 📂 Project Structure

etl_project/
│
├── data/
│   └── sales.csv
├── load_csv_pg.py
├── .dlt/
│   └── secrets.toml
└── README.md

---

## ⚙️ Features

* Extract data from CSV
* Data cleaning (column formatting, duplicates removal)
* Automatic table creation in PostgreSQL
* Seamless data loading using dlt

---

## 🔐 Configuration

Update `.dlt/secrets.toml` with your PostgreSQL credentials:

[destination.postgres.credentials]
host = "localhost"
port = 5432
username = "postgres"
password = "your_password"
database = "etl_db"

---

## ▶️ How to Run

1. Install dependencies:
   pip install dlt pandas psycopg2-binary

2. Run the pipeline:
   python load_csv_pg.py

---

## 🧪 Output

* Data will be loaded into PostgreSQL:
  Schema: etl_data
  Table: sales

* Verify using SQL:
  SELECT * FROM etl_data.sales;

---

## 💼 Use Case

This project simulates a real-world ETL pipeline used in data engineering for ingesting and processing structured data.

---

## 🚀 Future Enhancements

* Incremental data loading
* Process control table
* Airflow scheduling
* Power BI dashboard integration
* AI-based query system (RAG)

---

## 👩‍💻 Author

Lakshmi
