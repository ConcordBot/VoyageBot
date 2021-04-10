import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help1(self, ctx):
        embed = discord.Embed(
            title=f"Here are some commands!",
            colour=discord.Colour.blue()
        )
        embed.add_field(name="mute", value="Mutes a member", inline=True)
        embed.add_field(name="unmute", value="Unmutes a member", inline=True)
        embed.add_field(name="kick", value="Kicks a member", inline=True)
        embed.add_field(name="ban", value="Bans a member", inline=True)
        embed.add_field(name="unban", value="Unban a member", inline=True)
        embed.add_field(name="userinfo", value="Shows info about a member", inline=True)
        embed.add_field(name="serverinfo", value="Shows info about the server", inline=True)
        embed.add_field(name="meme", value="Shows a meme", inline=True)
        embed.add_field(name="rules", value="Shows you the rules of the server", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))