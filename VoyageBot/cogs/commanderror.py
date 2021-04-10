import discord
from discord.ext import commands

class CommandError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f"There was a command Error! :alert:")

def setup(bot):
    bot.add_cog(CommandError(bot))