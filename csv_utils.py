import random
import csv

def get_random_text_from_csv(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        return random.choice(rows)[0]