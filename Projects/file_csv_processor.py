#read csv & columns
import pandas as pd
import requests

# Read CSV file (replace 'your_file.csv' with the actual file path)
csv_file_path = 'chatgpt_search.csv'
df = pd.read_csv(csv_file_path)
col_Names = ['action','dataToProcess']
# Choose the column you want to send to the GPT API
selected_column = df[col_Names[0]]
#print(df)
print('---col1---')
print(selected_column)
datavals = df[col_Names[1]].tolist();

print('--data-vals---')
for i in datavals:
    print('my val' + i + ' ' )