# CSV Statistics Analyzer

A Python tool that analyzes CSV datasets, calculates useful statistics, and exports the results to Excel.

## Features

- reads CSV files
- automatically detects numeric columns
- calculates:
  - count
  - missing values
  - sum
  - mean
  - median
  - min
  - max
  - standard deviation
- exports raw data and statistics to an Excel report
- can also generate sample test data

## Project Structure

```text
CSV_Statistics_Analyzer/
├── analyze_csv.py
├── generate_test_data.py
├── test_data.csv
├── requirements.txt
├── README.md
└── .gitignore