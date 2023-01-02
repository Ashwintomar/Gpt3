import os
from dotenv import load_dotenv
import openai
load_dotenv()
from dotenv import load_dotenv




openai.api_key = os.getenv("OPENAI_API_KEY")
prompt_user = "prompt"
character = input("\nEnter a character you want to talk to : \n")

while(prompt_user != "stop"):
    prompt_user = input('\nEnter a prompt, to stop type stop.\n')
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="chat with me as "+character+"\n\nme: "+prompt_user+"\"\nmom:",
    temperature=0,
    max_tokens=30,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
    )
    text_res = response['choices'][0]['text']
    print(text_res+"\n")