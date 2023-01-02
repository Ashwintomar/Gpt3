import os
from dotenv import load_dotenv
import openai
load_dotenv()
from dotenv import load_dotenv



openai.api_key = os.getenv("OPENAI_API_KEY")
prompt_user = "prompt"



prompt_user = input('\nEnter a prompt\n')
response = openai.Completion.create(
model="code-davinci-002",
prompt="Create a nodejs server",
temperature=0,
max_tokens=100,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)
code_res = response['choices'][0]['text']
print(code_res)