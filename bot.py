import discord
import os
import io
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='c.')
bot.remove_command('help')
developers = [
        311970805342928896,
        316586772349976586,
        292690616285134850
    ]

@bot.event
async def on_ready():
    ctx.send("Bot Is Online")
    await bot.change_presence(game=discord.Game(name="c.help"))
        
@bot.command()
async def help(ctx):
    em = discord.Embed()
    em.title = "Help"
    em.description = "A bot under development by Antony, Sleedyak and Free TNT. Feel free to drop into the server and help with development and for support at https://discord.gg/qv9UcBh \n"
    em.add_field(name="Ping", value="Pong! check if bot is working")
    await ctx.send(embed=em)

@bot.command()
async def ping(ctx):
    """Pong! check if bot working"""
    em = discord.Embed()
    em.title = "Pong!"
    em.description = f'{bot.ws.latency * 1000:.4f} ms'
    await ctx.send(embed=em)

if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
