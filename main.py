import discord
import os
import asyncio
from discord.ext import commands

bot = commands.Bot("sarah.", intents=discord.Intents.all(), application_id="1111290476918755359")


if __name__ == "__main__":
    print(discord.__version__)
    for extension in os.listdir(os.fsencode("extensions")):
        if os.fsdecode(extension).endswith(".py"):
            try:
                asyncio.run(bot.load_extension(f"extensions.{os.fsdecode(extension)[:-3]}"))
            except:
                print(f"Die extension {os.fsdecode(extension)[:-3]} konnte nicht geladen werden.")
                raise

@bot.event
async def on_ready():
    print("Bot ist ready!")
    await bot.change_presence(activity=discord.Streaming(name="Sarah", url="https://www.twitch.tv/thatsshy"))

bot.run("MTExMTI5MDQ3NjkxODc1NTM1OQ.G1CWt0.BTNT8_wmvhj0Mhvtw5ilMNcc1rLin9GWuHK0MA")