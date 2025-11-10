import discord
from discord.ext import commands, tasks
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
    send_message.start()

@tasks.loop(minutes=30)
async def send_message():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(get_percent_changes("SPY"))
    else:
        print(f"Channel not found.")

bot.run(TOKEN)