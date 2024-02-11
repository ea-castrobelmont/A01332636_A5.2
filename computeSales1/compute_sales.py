#!/usr/bin/env python

""" computeSales """

import json
import sys
import time


def load_json_file(file_path):
    """Function printing python version."""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        sys.exit(1)


def compute_total_cost(price_catalogue, sales_record):
    """Function printing python version."""
    total_cost = 0
    for sale in sales_record:
        product = sale['Product']
        quantity = sale['Quantity']
        for item in price_catalogue:
            if item['title'] == product:
                product_price = item['price']
                total_cost += product_price * quantity
                break
        else:
            print(f"Warning: '{product}' not found in the price catalogue.")
    return total_cost


def main():
    """Main function for the computeSales script."""
    if len(sys.argv) != 3:
        print("Usage: computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    price_catalogue = load_json_file(price_catalogue_file)
    sales_record = load_json_file(sales_record_file)

    total_cost = compute_total_cost(price_catalogue, sales_record)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Time Elapsed: {execution_time:.2f} seconds")

    with open('SalesResults.txt', 'w', encoding="utf-8") as results_file:
        results_file.write(f"Total Cost: ${total_cost:.2f}\n")
        results_file.write(f"Time Elapsed: {execution_time:.2f} seconds\n")


if __name__ == "__main__":
    main()
