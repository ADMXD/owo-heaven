import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "!!"

#use the .env feature to hide your token

keep_alive()
token = os.getenv("TOKEN")

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)






@bot.event
async def on_ready():
    activity = discord.Game(name="TheDawn ", type=4)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     

{Fore.GREEN}

░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░░█████╗░███╗░░██╗██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗████╗░██║██║░██╔╝██╔════╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║██║░░██║███████║██╔██╗██║█████═╝░█████╗░░██████╔╝
██╔══██║██║░░░██║░░░██║░░░██║░░██║██║░░██║██╔══██║██║╚████║██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝██║░░██║██║░╚███║██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

selfbot is ready!
''')


















@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="<a:817489614326595644:856591733143765023> Help AutoOwO <a:817489614326595644:856591733143765023>",
        color=420699,
        description=
        f"<a:arrow2:856590874036666378>**{prefix}autoOwO**\nowoh, owo sell all, owo flip 500 and owo cash 50 seconds.\n\n**<a:arrow2:856590874036666378>{prefix}stopautoOwO**\nstops autoOwO.\n\n**<a:arrow2:856590874036666378>{prefix}Owobanbypass**\nIts prevent you from banning Owo by taking appropriate time\n Example:-`the bot takes breaak 5 min of runnning 1st break= 5min,2nd break=10min 3rd break=15min` \n\n made by Ari.6435"
    )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/icons/856358420385759293/a_c9bb8d2dd31eae42a2a9d6efc010e1bc.png"
    )
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO  is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(2)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(2)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(1)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(2)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(3)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(1)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(5)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(2)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(3)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(2)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(2)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(5)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(5)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(1)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(6)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(6)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(5)






@bot.command(pass_context=True)
async def Owobanbypass(ctx):
    await ctx.message.delete()
    await ctx.send('owobanbypass is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(2)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(2)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(1)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(2)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(3)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(1)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(5)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(2)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(3)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(2)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(2)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(5)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(5)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(1)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(6)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(1)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully owob")
            await asyncio.sleep(6)
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(5)
            
# @bot.command()
# async def stopautoOwO(ctx):
#     await ctx.message.delete()
#     await ctx.send('auto OwO Magi is now **disabled**!')
#     global dmcs
#     dmcs = False



















































keep_alive()
bot.run(token, bot=False)
