import discord
import DiscordUtils
from discord.ext import commands
import youtube_dl
import os
import aiohttp
import random

Token = "YOUR_TOKEN"
YOUR_PREFIX = "~"
client = commands.Bot(command_prefix=YOUR_PREFIX)


players = {}
music = DiscordUtils.Music()


@client.event
async def on_message(message):
    """ some on_message command """
    if message.author.id == client.user.id:
        return
    msg_content = message.content.lower()

    curseWord = ['curse1', 'curse2']  # deletes these words

    if any(word in msg_content for word in curseWord):
        await message.delete()
        
        
@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    # id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name,
        description=description,
        color=discord.Color.blurple()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    # embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


@client.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("You are not in a voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
        await ctx.send("disko has arrived!")
    else:
        await ctx.voice_client.move_to(voice_channel)
        
        
@client.command()
async def play(ctx, url: str):
    await ctx.send("Getting ready to play...")
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("disko is already playing. Use 'stop' command to end.")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')

    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("disko is now paused.")
    else:
        await ctx.send("disko is not playing any audio though!")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send("disko is now playing.")
    else:
        await ctx.send("disko is already playing.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("disko has been stopped.")
    os.remove("song.mp3")
    
    
@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        await ctx.send("till we meet again...")
    else:
        await ctx.send("disko is not connected to a voice channel.")

   
@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="Haha, Meme go brr", description="Here's your little meme")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
            

client.run(Token)
