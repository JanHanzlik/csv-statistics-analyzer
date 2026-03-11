import csv
import random

rows = 5000

with open("test_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # header
    writer.writerow([
        "id",
        "sales",
        "expenses",
        "profit",
        "customers",
        "temperature"
    ])

    for i in range(rows):
        sales = round(random.uniform(100, 1000), 2)
        expenses = round(random.uniform(50, 700), 2)
        profit = round(sales - expenses, 2)
        customers = random.randint(5, 120)
        temperature = round(random.uniform(15, 35), 1)

        writer.writerow([
            i + 1,
            sales,
            expenses,
            profit,
            customers,
            temperature
        ])

print("Test CSV generated: test_data.csv")