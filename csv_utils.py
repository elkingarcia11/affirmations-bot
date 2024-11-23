import random
import csv

def get_random_text_from_csv(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        return random.choice(rows)[0]
# Example Usage
"""
filepath = "example.csv"  # Update this with the correct path to your CSV file
random_text = get_random_text_from_csv(filepath)
if random_text:
    print(f"Random Text: {random_text}")
"""