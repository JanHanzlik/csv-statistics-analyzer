import pandas as pd
import sys
from pathlib import Path


def analyze_csv(input_file: str, output_file: str = "output_report.xlsx"):

    df = pd.read_csv(input_file)

    numeric_df = df.select_dtypes(include=["number"])

    stats = pd.DataFrame({
        "column": numeric_df.columns,
        "count": numeric_df.count().values,
        "missing_values": numeric_df.isna().sum().values,
        "sum": numeric_df.sum().values,
        "mean": numeric_df.mean().values,
        "median": numeric_df.median().values,
        "min": numeric_df.min().values,
        "max": numeric_df.max().values,
        "std_dev": numeric_df.std().values
    })

    # CSV export
    df.to_csv("raw_data_output.csv", index=False)
    stats.to_csv("statistics_output.csv", index=False)

    # Excel export
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Raw Data", index=False)
        stats.to_excel(writer, sheet_name="Statistics", index=False)

    print("Excel report created")


if __name__ == "__main__":

    input_csv = sys.argv[1] if len(sys.argv) > 1 else "test_data.csv"
    output_excel = sys.argv[2] if len(sys.argv) > 2 else "output_report.xlsx"

    if not Path(input_csv).exists():
        print("CSV file not found")
    else:
        analyze_csv(input_csv, output_excel)