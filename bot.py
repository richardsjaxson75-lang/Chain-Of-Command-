
import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Chain of Command bot is online as {bot.user}")

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        print(f"Roles changed for {after.display_name}")

@bot.command()
@commands.has_permissions(administrator=True)
async def coc(ctx):
    await ctx.send(
        "📋 **CFSRP Chain of Command**\n"
        "Leadership role changes are being monitored.\n"
        "The full chain of command still needs to be configured."
    )

if not TOKEN:
    raise RuntimeError("Please configure DISCORD_TOKEN in your environment.")

bot.run(TOKEN)
