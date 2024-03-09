# Requests is used with our chat gpt responses
import requests
from bot.utils.constants import CONST

# The url we will be using to send our prompt to the bot
gpt_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CONST.GPT_KEY}"
}


# Our method to get a response from our bot
def get_response_gpt(prompt):

  # Data to send
  data = {
      "model": CONST.GPT_MODEL,
      "messages": [{
          "role": "user",
          "content": prompt
      }],
      "temperature": CONST.GPT_TEMPERATURE
  }

  # Send the request
  response = requests.post(CONST.GPT_URL, json=data, headers=gpt_headers)
  if response.status_code == 200:
    return response.json()['choices'][0]['message']['content']
  else:
    return f"Wassah bruv, this is the developer. Thought I oughta let you know your request failed with status code {response.status_code}: {response.text}"
