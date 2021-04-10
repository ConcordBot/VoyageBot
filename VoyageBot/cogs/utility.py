import sys
import discord
import datetime
import psutil as psutil
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Utility came online at {datetime.datetime.now()}")

    @commands.command()
    async def serverinfo(self, ctx):
        """Displays server information."""
        guild = ctx.guild
        embed = discord.Embed(name="{}'s info".format(ctx.guild.name), color=0x176cd5)
        embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
        embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=True)
        embed.add_field(name="Members", value=len(ctx.guild.members))
        embed.add_field(name="Channels", value=len(ctx.guild.channels))
        embed.add_field(name="Region", value=ctx.guild.region)
        embed.add_field(name="Verification Level", value=ctx.guild.verification_level)
        embed.add_field(name="Owner", value=guild.owner)
        embed.add_field(name="Emojis", value=len(ctx.guild.emojis))
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text="Server ID is " + (str(ctx.guild.id)))
        await ctx.send(embed=embed)


    @commands.command(aliases=["ui"])
    @commands.guild_only()
    async def userinfo(self, ctx, user: discord.Member = None):
        """Gets some info about a user"""
        if not user:
            user = ctx.author
        member_number = sorted(ctx.guild.members, key=lambda m: m.joined_at).index(user) + 1
        em = discord.Embed(color=0xff0000)
        em.title = "User Info"
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Nickname", value=user.nick)
        em.add_field(name="Member Number", value=member_number)
        if user.activity:
            em.add_field(name="Activity", value=user.activity.name)
        em.add_field(name="User ID", value=str(user.id))
        time = user.joined_at.strftime("%A %h %d/%m/%Y")
        days = (datetime.datetime.now() - user.joined_at).days
        created_time = user.created_at.strftime("%A %h %d/%m/%Y")
        created_days = (datetime.datetime.now() - user.created_at).days
        em.add_field(name="Joined at", value=f"{time} ({days} Days ago!)")
        em.add_field(name="Account Created At", value=f"{created_time} ({created_days} Days ago!)")
        em.add_field(name="Status", value=user.status.name.title())
        await ctx.send(embed=em)


    @commands.command(pass_context=True)
    async def avatar(self, ctx, user: discord.Member = None):
        """Displays users avatar."""
        if not user:
            embed = discord.Embed(color=0x176cd5)
            embed = discord.Embed(title="View full image.", url=ctx.author.avatar_url, color=0x176cd5)
            embed.set_image(url=ctx.message.author.avatar_url)
            embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0x176cd5)
            embed = discord.Embed(title="View full image.", url=user.avatar_url, color=0x176cd5)
            embed.set_image(url=user.avatar_url)
            embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(Utility(bot))