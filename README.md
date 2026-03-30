# Sales_ETL_Python

This project simulates data pipeline for processing sales data.

## Pipeline Steps
- Extract: load raw sales data from CSV
- Transform:
  - remove missing values
  - filter invalid records (e.g. zero quantity)
  - calculate revenue (price * quantity)
- Load: store cleaned data in SQLite database
- Analyze: calculate total revenue per country

## Technologies
- Python
- Pandas
- SQLite
- SQL

## How to run
pip install -r pandas
python pipeline.py