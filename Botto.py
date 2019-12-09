import discord
from discord.ext import commands

client = commands.Bot(command_prefix ='.')

import random


@client.event
async def on_ready():
    #await client.change_presence(status=discord.Status.idle, activity=discord.Game('Game'))
    print("Botto is Ready.")

@client.event 
async def on_member_join(member):
    await member.create_dm() #https://discord.gg/XKnT4vJ
    await member.dm_channel.send(
        f'Welcome {member.name}, to the Super Novice Adventure Discord.\n If you have any quetions then ask someone else.'
    )


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def thanksgiving(ctx):
    await ctx.send(f'Happy Thanks Giving!!')

@client.command()
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else: 
            raise


client.run('DISCORD_TOKEN')