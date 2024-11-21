import random
import csv

# Read input from csv file
def read_csv_from(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)  # Read all rows into a list

# Get one random text from csv file
def get_random_text_from_csv(filepath):
    data = read_csv_from(filepath)
    text = random.choice(data)
    return text