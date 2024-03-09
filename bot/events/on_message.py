from bot.commands.stevie import stevie_bot
from bot.utils.constants import CONST
from bot.utils.correction import needs_correction
import discord


# When a message is sent, check its contents, and correct it if it references M
async def on_message(bot, message):

  # Check if the message is from the bot itself
  if message.author == bot.user:
    return

  # Get the specific user we will mention later
  id = int(CONST.USER_ID)

  predefined_user = message.guild.get_member(id) if \
  isinstance(message.channel, discord.TextChannel) else None
  user_name = predefined_user.mention if predefined_user else CONST.PREDEF_USERNAME

  # If the name m is there, correct it
  if needs_correction(message.content):
    author = message.author.mention
    response = f'Hey {author}, you mentioned M. Did you mean {user_name}?'
    await message.channel.send(response)

  # If it isn't we can try to respond with chat gpt :)
  else:

    # Respond as stevie!
    await stevie_bot(bot, message)
