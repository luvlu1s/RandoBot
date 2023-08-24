import discord
from discord.ext import commands 
import asyncio
import random

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

#update activity
async def update_activity():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers"))
        await asyncio.sleep(30)

@bot.slash_command(name='about', description='About RandoBot')
async def about(ctx):
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title = "About RandoBot", 
        description = "Randobot - Instant randomness for Discord choices! Try `/picknumber` and decide in a flash.",
        colour = discord.Colour.orange())
    embed.add_field(name=f"**Information**", value=f"<:arrow:1144369864811745422> **Developer:** [luvlu1s](https://omsdli.xyz)", inline=False)

    embed.add_field(name="**Statistics**", value=f"<:arrow:1144369864811745422> **Servers:** {len(bot.guilds)}\n<:arrow:1144369864811745422> **Users:** {sum(len(guild.members) for guild in bot.guilds)}\n<:arrow:1144369864811745422> **Latency:** {latency}ms", inline=False)

    embed.add_field(name=f"**Support**", value=f"**<:arrow:1144369864811745422> [Buy me a Coffee](https://www.buymeacoffee.com/oms.blink)**")
    await ctx.respond(embed=embed)

@bot.slash_command(name="picknumber", description="Pick between 1-100")
async def picknumber(ctx, first_num: int, second_num: int):
    if first_num > second_num:
        await ctx.respond(f"The first number should be smaller than the second number!")
        return
    random_number = random.randint(first_num, second_num)
    await ctx.respond(f"Results: {random_number}")
    

@bot.event
async def on_ready():
    print(f'Log in as {bot.user}')
    await update_activity() 
    
def run_discord_bot():
    TOKEN = '' #your bot token here
    bot.run(TOKEN)