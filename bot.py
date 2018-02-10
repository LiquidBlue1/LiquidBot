#dicordbot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context = True)
async def c(ctx, number):
    mgs = [] 
    number = int(number) 
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)



bot.run(process.env.BOT_TOKEN);