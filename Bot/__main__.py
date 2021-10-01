# __main__.py
import discord
from discord.ext import commands
import os
import dotenv

__version__ = "1.0"
# Setup
print(discord.__version__)
intents = discord.Intents().all()
intents.members = True
dotenv.load_dotenv()

MY_ID      = 893336301967900702
TOKEN      = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
USER_ID    = os.getenv('USER_ID')
PHRASE     = os.getenv('PHRASE')
MESSAGE    = "{user} it is your turn :)"

# Settings
bot = commands.Bot(command_prefix="?",intents = intents)

# Events
@bot.event
async def on_ready():
    print(f"{bot.user.name} v{__version__}, connected to discord.")

@bot.event
async def on_message(message):
    print(message.content)
    print(message.author.id)
    print("----------------")
    if (message.channel.id == CHANNEL_ID and PHRASE in message.content and message.author.id != MY_ID):
        user = bot.get_user(USER_ID)
        await message.channel.send(MESSAGE.format(user=user.mention))


bot.run(TOKEN)
