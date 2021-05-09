#import os
#from dotenv import load_dotenv
#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')


import discord 
from discord.ext import commands 


#TOKEN = 'ODQwNzkwMDU1Mjc0ODA3MzI4.YJdUwg.-0TILbGGzoY5i1EuTJLDvlst5e0'
bot = commands.Bot(command_prefix = '/')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"Nuestros Link: \n", 
    description=" Instagram: https://www.instagram.com/technovationchile/ \n BlackBoard: https://us.bbcollab.com/guest/f1a01c330844439fa1db5d0c108aa364")
    await ctx.send(embed=embed)

@bot.command()
async def saludar(ctx):
    await ctx.send('Hola, quisieramos conocerte, Presentate!')

@bot.command()
async def pres(ctx, nombre: str , edad:int):
    await ctx.send('Tu Nombre es: ' +str(nombre) + '\nTu edad es: ' +str(edad))# + int(edad))


@bot.event
async def on_ready():
    print("Bot is Ready")
    await bot.change_presence(activity=discord.Streaming(name="@technovationchile", url="https://www.instagram.com/technovationchile/"))

bot.run(TOKEN)