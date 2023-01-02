import os
from dotenv import load_dotenv
import openai
load_dotenv()
from dotenv import load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


