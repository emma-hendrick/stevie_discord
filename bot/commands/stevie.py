import discord
from bot.gpt.prompt_gpt import get_response_gpt
from bot.utils.constants import CONST


# Respond to a message with chatGPT
async def stevie_bot(bot, message):

  dm = isinstance(message.channel, discord.DMChannel)

  # If the message is a DM, process it as is
  if dm:
    async with message.channel.typing():
      await process_input(bot, message, message.content.strip())

  # If the message is in a text channel, only process the part following the command
  elif '!stevie ' in message.content[:8].lower():
    async with message.channel.typing():
      await process_input(bot, message, message.content[8:].strip())


async def process_input(bot, message, user_prompt):

  # Get the bot name and user name
  bot_name = bot.user.name if bot.user else CONST.PREDEF_BOTNAME
  user_name = message.author.display_name

  # Request a response from chat gpt
  gpt_prompt = f'Give me an quippy response (from the view of {bot_name} who is a 10 year old discord bot, hosted as a repl on replit) to the discord message, \'{user_prompt}\', from {user_name}. Only provide me with the response, nothing else.'
  gpt_response = get_response_gpt(gpt_prompt)

  # Log the message, user, and channel it was sent in
  print(
      f"Message from {message.author}: \"{user_prompt}\" in {message.channel}. Response: {gpt_response}"
  )

  # Respond to the user
  await message.channel.send(
      gpt_response if gpt_response else
      'Sorry, I\'m having trouble understanding your message.')
