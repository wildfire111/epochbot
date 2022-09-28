import datetime
import discord
from discord.ext import commands
import os
import time
import asyncio
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('GUILD_ID')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

def update():
    print('updating')
    current = (datetime.datetime.utcnow())
    weekday = current.weekday()
    if weekday <= 2:
        offset = 2-weekday
    elif weekday > 2:
        offset = 9-weekday
    offsetobj = datetime.timedelta(days=offset)
    target = datetime.datetime(current.year,current.month,current.day,hour=23,minute=59)-offsetobj
    remaining = (target-current).seconds
    minutes = remaining // 60
    seconds = remaining % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    nickname = f'UwUpoch end: {target.month}/{target.day}/{target.year} {target.hour}:{target.minute}'
    status = f'Remaining: {days}D {hours}H {minutes}M'
    await bot.get_guild(guild).me.edit(nick=nickname)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
    time.sleep(60)
    update()

async def on_ready():
    await update()

bot.run(token)