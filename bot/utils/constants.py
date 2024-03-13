# OS allows us to retrieve our evironment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load variables from .env
dotenv_path = join(dirname(__file__), "../../.env")
print(dotenv_path)
load_dotenv(dotenv_path)

# All the program constants
class CONST:
  DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
  USER_ID = os.environ['USER_ID']
  GPT_KEY = os.environ['GPT_KEY']
  GPT_URL = 'https://api.openai.com/v1/chat/completions'
  GPT_MODEL = 'gpt-3.5-turbo'
  GPT_TEMPERATURE = 0.7
  GPT_ERROR_MESSAGE = 'Sorry, I\'m having trouble understanding your message.'
  PREDEF_USERNAME = 'Emma'
  PREDEF_BOTNAME = 'Stevie the Wonderbot'
  CORRECTION_REGEX = r'\b(?<![\`\‘\’\'])[mM]\b'
