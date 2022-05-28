import discord
from discord.ext import commands
import os
import requests
import random
import time
import xlsxwriter
import pandas as pd
import xlrd
import openpyxl

client = commands.Bot("!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('callbot commands'):
      await message.channel.send('The commands are: callbot commands - commands, callbot rickroll - bot sends rickroll, callbot meme - bot sends meme, callbot rr - try your luck, die = get kicked, niggers are bad - bot replies, gays are faggots - bot replies, sieg heil - bot hails the fuhrer, i rape jews - bot replies, tell me a fact - bot replies, sus - bot ejects you from the server, callbot id - bot adds you to the cash database and gives you your ID')
    
    if message.content.startswith('callbot rickroll'):
        await message.channel.send('Here is the link.')
        embed=discord.Embed(title="HOW TO GET 1 MILLION DOLLARS FOR FREE (WORKING 2022 😱😱)", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="FREE MONEY GLITCH IN REAL LIFE??? 😱😱😱", color=0xFF5733)
        await message.channel.send(embed=embed)

    if message.content.startswith('callbot meme'):
        response=requests.get("http://meme-api.herokuapp.com/gimme/dankmemes")
        link  = response.json()['url']
        print(link)
        img_data = requests.get(link).content
        with open('meme.jpg', 'wb') as handler:
          handler.write(img_data)
        await message.channel.send(file = discord.File('meme.jpg'))

    if message.content.startswith('callbot rr'):
        await message.channel.send('Firing...')
        time.sleep(0.5)
        randomChance = random.randint(0,5)
        if randomChance == 5:
          await message.channel.send('You died...')
          await kick(client, message.author, reason="Russian Rouletted")
          await message.channel.send(f'{message.author.name} got Russian Roulleted (by me)')
        elif randomChance <= 4:
          df = pd.read_excel("db.xlsx").set_index("ID")
          if message.author.id in df.index:
            df.loc[message.author.id, "Cash"] += 5 
          else:
            df.loc[message.author.id] = [5, 0]
          await message.channel.send('You lived. Added 5 dollars to account.')
          await message.channel.send('Current balance: ' + str(df["Cash"][message.author.id]) + " dollars")
          df.to_excel("db.xlsx")
        else:
          await message.channel.send('how the fuck did this happen')

    if message.content.startswith('niggers are bad'):
      await message.channel.send('I dont like black people too.')
      
    if message.content.startswith('gays are faggots'):
      await message.channel.send('Imagine being LGBT cant relate LMAO.')

    if message.content.startswith('sieg heil'):
      await message.channel.send('All hail the Fuhrer.')

    if message.content.startswith('i rape jews'):
      await message.channel.send('Me too! In fact I lie and say to the court that the jew raped me!')

    if message.content.startswith('tell me a fact'):
      await message.channel.send('All girls are either bipolar or bisexual.')

    if message.content.startswith('L + ratio'):
      await message.channel.send('no u')
      await kick(client, message.author, reason="counter ratio")

    if message.content.startswith('sus'):
      await message.channel.send('among us is shit')
      await kick(client, message.author, reason="u got ejected bitch")
      await message.channel.send(f'{message.author.name} got ejected.')

    if message.content.startswith('callbot id'): 
      df = pd.read_excel("db.xlsx").set_index("ID")
      if message.author.id not in df.index:
        df.loc[message.author.id] = [0, 0]
      print(df)
      df.to_excel("db.xlsx")
      
      await message.channel.send(message.author.display_name + " has " + str(df["Cash"][message.author.id]) + " dollars and " + str(df["Points"][message.author.id]) + " points")

client.run(os.getenv('TOKEN'))