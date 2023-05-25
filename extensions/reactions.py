import asyncio
import discord
from discord.ext import commands

class Reactions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Reactions geladen!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if "guten morgen" in message.content.lower():
                await message.reply("Guten Morgen!")

            if "sarah" in message.content.lower():
                await message.add_reaction("<a:nom:1096037258697654453>")

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        await channel.send(f"{user.name} is typing... undzwar {when}")

async def setup(bot):
    await bot.add_cog(Reactions(bot))