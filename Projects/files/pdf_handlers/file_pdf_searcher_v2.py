import os
import json
import PyPDF2
import csv
from datetime import datetime

# Load config
with open('pdf_analyzer_config.json', 'r') as f:
    config = json.load(f)

search_words = config['search_words']
pdf_folder = config['pdf_folder']
output_folder = config.get('output_folder', '.')

def search_pdf(file_path, search_words):
    results = {word: False for word in search_words}
    try:
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text = page.extract_text() or ""
                for word in search_words:
                    if word.lower() in text.lower():
                        results[word] = True
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return results

found_files = []
not_found_files = []

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith('.pdf'):
        file_path = os.path.join(pdf_folder, filename)
        found_words = search_pdf(file_path, search_words)
        if any(found_words.values()):
            found_files.append((filename, found_words))
        else:
            not_found_files.append((filename, found_words))

# Create output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Generate CSV filename with keywords and timestamp
keywords_part = "_".join([w.replace(" ", "_") for w in search_words])
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_filename = f"{keywords_part}_{timestamp}.csv"
csv_path = os.path.join(output_folder, csv_filename)

with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Filename'] + search_words
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    def print_and_write(file_list):
        for filename, found_words in file_list:
            row = {'Filename': filename}
            row.update({word: 'Found' if found else 'Not Found' for word, found in found_words.items()})
            writer.writerow(row)

            # Print to console
            print(f"File: {filename}")
            for word in search_words:
                print(f"  - '{word}': {row[word]}")
            print()

    print_and_write(found_files)
    print_and_write(not_found_files)

print(f"Results written to {csv_path}")
