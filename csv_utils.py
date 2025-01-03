import random
import csv

def get_random_text_from_csv(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        return random.choice(rows)[0]
    
def remove_end_period(input_file, output_file):
    # Process the CSV file
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            # Remove last character if it's a period
            updated_row = [col[:-1] if col.endswith('.') else col for col in row]
            writer.writerow(updated_row)