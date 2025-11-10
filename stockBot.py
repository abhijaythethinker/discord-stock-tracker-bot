import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from stockTracker import get_percent_changes

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(get_percent_changes("EVMN"))

bot.run(TOKEN)