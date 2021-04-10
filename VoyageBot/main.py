import os
import discord
import datetime
import config
from discord.ext import commands



bot = commands.Bot(command_prefix=config.PREFIX)



sep = '________________________________________________________________'

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Voyage Development', url='https://www.twitch.tv/your_channel_here'))
    bot.remove_command('help')
    print(sep)
    print(sep)
    print(f"Logged in as {bot.user.name}")
    print(sep)
    print(sep)
    print(f"Came online at {datetime.datetime.now()}")
    print(sep)
    print(sep)
    print(f"Currently in Watching Voyage Development")
    print(sep)
    print(sep)
    print(f"Watching commands in servers!")
    print(sep)
    print(sep)





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

    else:
        print(f'Unable to load {filename[:-3]}')



bot.run(config.TOKEN)