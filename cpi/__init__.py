"""
Adjusts dollar figures for inflation using the Consumer Price Index.
"""
import os
import csv

this_dir = os.path.dirname(__file__)
csv_path = os.path.join(this_dir, 'cpi.csv')

data = csv.DictReader(open(csv_path, "r"))

cpi = dict(
    (int(r['Year']), float(r['Value'])) for r in data 
)

def to_2016_dollars(value, year, to_year=2016):
    if year == 2017:
        return value
    return (value * cpi[to_year]) / cpi[year] 
