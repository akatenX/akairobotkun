import discord
from discord.ext import tasks, commands
from ping3 import ping
from googlesearch import search
import asyncio
import requests
import json
import sys
import urllib.request
import socket
import random
import string





# token.txtを読み込み
file=open('token.txt')
tokens=file.read()
TOKEN = tokens
file.close()
bot = commands.Bot(command_prefix="-", case_insensitive=True, help_command=None)

presence = discord.Game("( ・∇・)！")

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
async def help(ctx):
    print("help")
    embed=discord.Embed(title="help", description="akairobotのhelpだよ！", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/970936654401527828/994242796292677733/64_20220706230033.png?width=667&height=667")
    embed.add_field(name="help", value="helpを表示するよ！", inline=True)
    embed.add_field(name="spam", value="spamするよ！ -spam スパムしたいメッセージ   回数だよ！", inline=True)
    embed.add_field(name="spamb", value="webhookでspamするよ！ 上のspamとほぼ同じだよ！", inline=True)
    embed.add_field(name="clear", value="メッセージを消すよ！ -clear   消す数だよ！", inline=True)
    embed.add_field(name="ping", value="使えないよ！", inline=True)
    embed.add_field(name="google", value="使えないよ！", inline=True)
    embed.add_field(name="time", value="今の時間を出すよ！ 3秒ぐらい遅れてるかも！", inline=True)
    embed.add_field(name="weather", value="天気を出すよ！ 合ってるかは知らないよ！", inline=True)
    embed.add_field(name="calc", value="計算するよ！ -calc tasu,hiku,kake,wari   数1  数2だよ！", inline=True)
    embed.add_field(name="trans", value="翻訳するよ！ -trans 元の言語   翻訳先の言語だよ！", inline=True)
    embed.add_field(name="short", value="urlを短縮するよ！ -url  短縮したいurlだよ！", inline=True)
    embed.add_field(name="botinfo", value="botの情報を表示するよ！", inline=True)
    embed.add_field(name="gen", value="何かをgenerateするよ！ -gen  genしたい物  数 だよ！", inline=True)

    embed.add_field(name="kick", value="kickするよ！", inline=True)
    embed.add_field(name="ban", value="banするよ！", inline=True)
    await ctx.send(embed=embed)




@bot.command()
@commands.has_permissions(administrator=True)
async def spamb(ctx, arg1, arg2):
    print("spamwebhook send" + arg1)
    """webhookでスパムする"""
    webhook_url  = 'https://discord.com/api/webhooks/000010201040245515841684'
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
    """time"""
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
    url = "https://api.openweathermap.org/data/2.5/weather?q=sapporo,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("札幌の天気は" + data['weather'][0]['description'])
    url = "https://api.openweathermap.org/data/2.5/weather?q=kushiro,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("釧路の天気は" + data['weather'][0]['description'])
    url = "https://api.openweathermap.org/data/2.5/weather?q=nigata,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("新潟の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=sendai,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("仙台の天気は" + data['weather'][0]['description'])
    url = "https://api.openweathermap.org/data/2.5/weather?q=kanazawa,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("金沢の天気は" + data['weather'][0]['description'])
    url = "https://api.openweathermap.org/data/2.5/weather?q=tokyo,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("東京の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=hiroshima,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("広島の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=nagoya,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("名古屋の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=fukuoka,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("福岡の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=osaka,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("大阪の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=kagoshima,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("鹿児島の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=kochi,jp&appid==ja&units=metric"
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("高知の天気は" + data['weather'][0]['description'])
    url = "http://api.openweathermap.org/data/2.5/weather?q=naha,jp&appid==ja&units=metric"
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


@bot.command()
async def trans(ctx, arg1, arg2, arg3):
    print("trans")
    """trans"""
    moto = str(arg3)
    url = "https://script.google.com//s/-/exec?text=" + moto + "&source=" + arg1 + "&target=" + arg2
    res = requests.get(url)
    data = json.loads(res.text)
    await ctx.send("翻訳の結果は" + data['text'] + "です")


@bot.command()
async def short(ctx, arg):
    print("short")
    url = 'https://..com/v1/?key=-_'
    data = {
        'longDynamicLink': 'https://akairo.page.link/?link=' + str(arg),
        'suffix': {
          'option': 'SHORT'
        }
    }
    headers = {
        'Content-Type': 'application/json',
    }
    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    body = json.loads(body)
    await ctx.send("短縮したよ！ urlは<" + body['shortLink'] + ">だよ！")


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def botinfo(ctx):
    print("botinfo")
    host = socket.gethostname()
    print(host)
    ip = socket.gethostbyname(host)
    print(ip)
    await ctx.send("host名は " + host + "でipは " + ip + "だよ！")

@bot.command()
async def gen(ctx, arg, arg2):
    print("gen")
    if arg == "nitro":
        print('nitro')
        for i in range(int(arg2)):
            a = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            await ctx.send("discord.gift/" + a)
    else:
        await ctx.send("対応しているのは nitro です")

@bot.command()
async def janken(ctx, arg):
    hand = ['グー', 'チョキ', 'パー']
    plhand = arg
    str(plhand)
    cpuhand = random.choice(hand)
    await ctx.send("あなた:" + plhand)
    await ctx.send("CPU:" + cpuhand)
    if plhand == cpuhand:
      print("あいこだよ！")
    else:
      if plhand == "グー":
        if cpuhand == "チョキ":
          await ctx.send("あなたの勝ち！")
        if cpuhand == "パー":
          await ctx.send("あなたの負け！")
      elif plhand == "チョキ":
        if cpuhand == "パー":
          await ctx.send("あなたの勝ち！")
        if cpuhand == "グー":
          await ctx.send("あなたの負け！")
      elif plhand == "パー":
        if cpuhan == "グー":
          await ctx.send("あなたの勝ち！")
        if cpuhand == "チョキ":
          await ctx.send("あなたの負け！")
      


bot.run(TOKEN)
