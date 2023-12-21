import pandas as pd
import requests

# Read CSV file (replace 'your_file.csv' with the actual file path)
csv_file_path = 'your_file.csv'
df = pd.read_csv(csv_file_path)

# Choose the column you want to send to the GPT API
selected_column = df['your_column_name']

# Join the values into a single string
text_to_generate = ' '.join(selected_column.astype(str))

# OpenAI GPT API endpoint
api_endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'

# OpenAI API key
api_key = 'your_api_key_here'

# Request headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

# Request payload
payload = {
    'prompt': text_to_generate,
    'max_tokens': 100,  # Adjust as needed
}

# Make the API request
response = requests.post(api_endpoint, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    generated_text = response.json()['choices'][0]['text']
    print("Generated Text:")
    print(generated_text)
else:
    print(f"Error {response.status_code}: {response.text}")
