import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from stockTracker import get_percent_changes

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

scheduler = AsyncIOScheduler()

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    
    if not scheduler.running:
        scheduler.start()

async def send_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(get_percent_changes("SPY"))
        await channel.send(get_percent_changes("QQQ"))
    else:
        print(f"Channel not found.")

scheduler.add_job(
    send_message,
    CronTrigger(
        day_of_week="mon-fri",
        hour="9-15",
        minute="35"
    )
)

bot.run(TOKEN)