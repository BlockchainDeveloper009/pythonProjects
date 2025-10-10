"""
should read the pdfs and look for search key words;
usecase: download bank statements, look for specific txn in a month,
year,
"""

import os
import json
import PyPDF2
script_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(script_dir, 'pdf_analyzer_config.json')
# Load config
with open(config_path, 'r') as f:
    config = json.load(f)

search_words = config['search_words']
pdf_folder = config['pdf_folder']

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

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith('.pdf'):
        file_path = os.path.join(pdf_folder, filename)
        found_words = search_pdf(file_path, search_words)
        print(f"File: {filename}")
        for word, found in found_words.items():
            print(f"  - '{word}': {'Found' if found else 'Not Found'}")
        print()
