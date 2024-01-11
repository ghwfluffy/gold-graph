#!/usr/bin/env python3

from datetime import datetime
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Qt5Agg')

def parse_date(date_string):
    try:
        return datetime.strptime(date_string, "%m/%d/%Y")
    except:
        pass

    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except:
        pass

    try:
        return datetime.strptime(date_string, "%a %b %d %Y")
    except:
        pass

    print("Invalidate date: '" + date_string + "'")

gold = []

with open("gold_prices.csv", "r") as fp:
    for line in fp:
        fields = line.split(",")

        date = fields[0]
        price_per_oz = fields[1]

        gold.append({
            'date': parse_date(date),
            'price': float(price_per_oz),
        })

homes = []
with open("median_home_value.csv", "r") as fp:
    for line in fp:
        fields = line.split(",")

        date = fields[0]
        price = fields[1]

        homes.append({
            'date': parse_date(date),
            'price': float(price)
        })

# Convert string dates to datetime objects and separate the prices
dates1 = [d['date'] for d in gold]
prices1 = [d['price'] * 32.15 * 6 for d in gold]

dates2 = [d['date'] for d in homes]
prices2 = [d['price'] for d in homes]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(dates1, prices1, label='6 kilograms of Gold')
plt.plot(dates2, prices2, label='Median US house price')

# Adding titles and labels
plt.title('Price Comparison Over Time')
plt.xlabel('Date')
plt.ylabel('Price USD')
plt.legend()
plt.show()
