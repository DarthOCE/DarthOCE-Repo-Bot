import discord
from discord import Embed, File
from discord.ext import commands

token = ""

client = commands.Bot(command_prefix='>')
client.remove_command('help')


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    discord.Activity(name=">help", type=1)


@client.command()
async def help(ctx):
    embed = Embed(title="All Commands", description="DarthOCE's Repo bot")
    embed.add_field(name=">help", value="Displays all available commands", inline=False)
    embed.add_field(name=">projects", value="Displays all current github projects", inline=False)
    embed.set_footer(text="Made by DarthOCE#8832")
    await ctx.send(embed=embed)


@client.command()
async def projects(ctx):
    embed = Embed(title="Projects", description="DarthOCE's Repo bot")
    embed.add_field(name="Jailbreak Repo", value="A Repository containing all my tweaks", inline=False)
    embed.add_field(name="Kahoot Botter", value="A Kahoot and Quizizz Botter", inline=False)
    embed.set_footer(text="Made by DarthOCE#8832")
    await ctx.send(embed=embed)
   

client.run(token)
