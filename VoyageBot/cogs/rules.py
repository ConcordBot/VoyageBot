import discord
from discord.ext import commands


class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rules(self, ctx):
        embed=discord.Embed(
            title="Here are the rules of the server",
            colour=discord.Colour.blue()
        )
        embed.add_field(name="No NSFW", value="No NSFW in this server", inline=True)
        embed.add_field(name="No Gore", value="Please don't post any Gore", inline=True)
        embed.add_field(name="Please be respectful to other members and staff", value="Don't disrespect any other members or staff", inline=True)
        embed.add_field(name="Please report all bad behaviour", value="Please DM or tell a staff member If there is any bad behaviour you could be rewarded.", inline=True)
        embed.add_field(name="Please Suggest suggestions", value="If you have an opinion on something feel free to DM a admin or owner", inline=True)
        embed.add_field(name="No Doxxing", value="Doxxing means exposing personal information. Please don't Dox anyone in this server", inline=True)
        embed.add_field(name="No Spamming", value="Please don't spam!'", inline=True)
        embed.add_field(name="Please Follow Discord's TOS", value="Please follow Discord TOS or you will be punished", inline=True)
        embed.add_field(name="Don't advertize", value="Please don't advertize your server in DMS or the server unless you are allowed to", inline=True)
        embed.add_field(name="Please post according to the channel", value="Please post the correct content in the correct channel", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Rules(bot))