import os
from dotenv import load_dotenv
import openai
load_dotenv()
from dotenv import load_dotenv




openai.api_key = os.getenv("OPENAI_API_KEY")
prompt_user = "prompt"



prompt_user = input('\nEnter a prompt\n')
response = openai.Image.create(
prompt=prompt_user,
n=1,
size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)