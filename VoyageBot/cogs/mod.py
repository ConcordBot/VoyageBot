import discord
import datetime
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Mod came online at {datetime.datetime.now()}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, error, mem: discord.Member, reason=None):
        guild = ctx.guild
        if mem == None:
            await ctx.send(f"Please define a member Next Time!")
        else:
            em = discord.Embed(
                title=f"{mem.display_name}#{mem.discriminator} has been banned for {reason}! his Id is {mem.id} if you want to unban him later",
                colour=discord.Colour.red()
            )
            if isinstance(error, error.MissingPermissions):
                await ctx.send(":redTick: You don't have permission to ban members.")
            await guild.ban(mem=mem)
            await ctx.send(em=em)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, error, mem: discord.Member):
        guild = ctx.guild
        if mem == None:
            await ctx.send(f"Please define a member Next Time!")
        else:
            em = discord.Embed(
                title=f"{mem.display_name}#{mem.discriminator} has been unbanned!",
                colour=discord.Colour.red()
            )
            if isinstance(error, error.MissingPermissions):
                await ctx.send(":redTick: You don't have permission to unban members.")
            await guild.unban(mem=mem)
            await ctx.send(em=em)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, error, mem: discord.Member, reason=None):
        guild = ctx.guild
        if mem == None:
            await ctx.send(f"Please define a member Next Time!")
        else:
            em = discord.Embed(
                title=f"{mem.display_name}#{mem.discriminator} has been kicked for {reason}!",
                colour=discord.Colour.red()
            )
            if isinstance(error, error.MissingPermissions):
                await ctx.send(":redTick: You don't have permission to kick members.")
            await guild.kick(mem=mem)
            await ctx.send(em=em)

    @commands.command(description="Mutes the specified user.")
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)
        embed = discord.Embed(title="muted", description=f"{member.mention} was muted ",
                              colour=discord.Colour.light_gray())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" you have been muted from: {guild.name} reason: {reason}")

    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(kick_members=True)
    async def unmute(ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await member.send(f" you have unmutedd from: - {ctx.guild.name}")
        embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",
                              colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send('Succes!')


def setup(bot):
    bot.add_cog(Mod(bot))