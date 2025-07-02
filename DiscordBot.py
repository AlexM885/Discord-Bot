import os
from dotenv import load_dotenv
import discord #interact with discord api
from discord.ext import commands #build command basd bot
load_dotenv()  # Load variables from .env file
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # read messages

bot = commands.Bot(command_prefix="!", intents=intents) #look for commands with !

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}") #bot logs into discord

@bot.command() #turns hello into a command
async def hello(ctx): #gives access to author channel message
    await ctx.send(f"Hi {ctx.author.name}! 👋")

bot.run(TOKEN)