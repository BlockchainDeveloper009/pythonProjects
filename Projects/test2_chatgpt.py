import os
from openai import OpenAI
# Set your OpenAI GPT API key


client = OpenAI(
    # This is the default and can be omitted
    # api_key=os.environ.get("OPENAI_API_KEY"),
    api_key = "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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)