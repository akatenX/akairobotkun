import discord
from discord.ext import tasks, commands
from ping3 import ping
from googlesearch import search
import asyncio
import requests
import json
import sys

TOKEN = "ここにtoken"
bot = commands.Bot(command_prefix="-", case_insensitive=True)

presence = discord.Game("discord.ext")

@bot.event
async def on_ready():
    await bot.change_presence(activity=presence)
    print("login")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def spam(ctx, arg1, arg2):
    print("spam send" + arg1)
    """スパムする"""
    for i in range(int(arg2)):
        await ctx.send(arg1)
       

@bot.command()
@commands.has_permissions(administrator=True)
async def spamb(ctx, arg1, arg2):
    print("spamwebhook send" + arg1)
    """webhookでスパムする"""
    webhook_url  = 'ここにwebhook'
    main_content = {
                   'username': 'akairobotwebhook',
                   'avatar_url': 'https://media.discordapp.net/attachments/970936654401527828/994242796292677733/64_20220706230033.png?width=667&height=667',
                   'content': arg1
               }
    headers      = {'Content-Type': 'application/json'}
    for i in range(int(arg2)):
        response     = requests.post(webhook_url, json.dumps(main_content), headers=headers)
        await asyncio.sleep(0.1)


        
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, num):
    print("message clear")
    """メッセージを消す"""
    async for message in ctx.channel.history(limit=int(num)+1):
        await message.delete()


@bot.command()
async def ping(ctx, arg1):
    print("ping" + arg1)
    """pingする"""
    a = ping(arg1, unit='ms')
    str(a)
    await ctx.send(f"{arg1}の結果は{a}です")


#時間
@bot.command()
async def time(ctx):
    print("time")
    url = "https://www.timeapi.io/api/Time/current/zone?timeZone=Asia/Tokyo"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("今の時間は" + str(data["hour"]) + "時" + str(data["minute"]) + "分" + str(data["seconds"]) + "秒だよ(この時間は少し遅れている可能性があります)")

#天気
@bot.command()
async def weather(ctx):
    print("weather")
    """weatherする"""
    url = "https://api.openweathermap.org/data/2.5/weather?q=sapporo,jp&appid=92fab0&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("札幌の天気は" + data['weather'][0]['description'])
    url = "https://api.openweathermap.org/data/2.5/weather?q=kushiro,jp&appid=92fab&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("釧路の天気は" + data['weather'][0]['description'])
    url = "https://api.openweathermap.org/data/2.5/weather?q=nigata,jp&appid=92fab2&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("新潟の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=sendai,jp&appid=92fab22370&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("仙台の天気は" + data['weather'][0]['description'])
    url = "https://api.openweathermap.org/data/2.5/weather?q=kanazawa,jp&appid=92fab23370&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("金沢の天気は" + data['weather'][0]['description'])
    url = "https://api.openweathermap.org/data/2.5/weather?q=tokyo,jp&appid=92fa370&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("東京の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=hiroshima,jp&appid=92fab70&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("広島の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=nagoya,jp&appid=92fab23170&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("名古屋の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=fukuoka,jp&appid=92fa370&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("福岡の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=osaka,jp&appid=92fab0&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("大阪の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=kagoshima,jp&appid=92fab70&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("鹿児島の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=kochi,jp&appid=&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("高知の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=naha,jp&appid=92fab70&lang=ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("那覇の天気は" + data['weather'][0]['description'])

    
#計算
@bot.command()
async def calc(ctx, arg, arg1, arg2):
    print("calc")
    """calcする"""
    if arg == "tasu":
        print('tasu')
        calc = int(arg1) + int(arg2)
        await ctx.send("計算結果は" + str(calc) + "です")
    elif arg == "hiku":
        print('hiku')
        calc = int(arg1) - int(arg2)
        await ctx.send("計算結果は" + str(calc) + "です")
    elif arg == "kake":
        print('kake')
        calc = int(arg1) * int(arg2)
        await ctx.send("計算結果は" + str(calc) + "です")
    elif arg == "wari":
        print('wari')
        calc = int(arg1) / int(arg2)
        await ctx.send("計算結果は" + str(calc) + "です")
    elif arg == "help":
        print('help')
        await ctx.send("tasu hiku kake wari help")
    else:
        print('calc nannmonai')


#google検索
@bot.command()
async def search(ctx, arg):
    print("google!")
    kensaku = arg
    count = 0
    # 日本語で検索した上位5件を順番に表示
    sea = search(str(kensaku), lang="jp")
    await asyncio.sleep(1)
    await ctx.send("計算結果は" + str(sea) + "です")


@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member, reason):
   await member.kick(reason=reason)
   embed=discord.Embed(title="KICK", color=0xff0000)
   embed.add_field(name="メンバー", value=f"{member.mention}", inline=False)
   embed.add_field(name="理由", value=f"{reason}", inline=False)
   await ctx.send(embed=embed)



@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member, reason):
   await member.ban(delete_message_days=7, reason=reason)
   embed=discord.Embed(title="BAN", color=0xff0000)
   embed.add_field(name="メンバー", value=f"{member.mention}", inline=False)
   embed.add_field(name="理由", value=f"{reason}", inline=False)
   await ctx.send(embed=embed)





bot.run(TOKEN)
