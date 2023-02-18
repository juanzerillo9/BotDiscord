import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from googletrans import Translator
import KeepAlive
import goslate 

translator = Translator()
session = HTMLSession()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
  print("online")


@bot.command(name="ping")
async def ping(ctx):
  await ctx.send("pong")


@bot.command(name="admins")
async def admins(ctx):
  await ctx.send("""
ADMINISTRADORES DEL SERVIDOR

JZ9        ->   www.instagram.com/j73z__/
RENJO   ->   www.instagram.com/weremczuk/

""")

@bot.command()
async def documentacion(ctx):
  await ctx.send("""
  
La documentacion del bot se encuentra disponible en:

https://github.com/juanzerillo9/BotDiscord/blob/main/Documentacion.txt

""")


@bot.command()
async def comandos(ctx):
  await ctx.send("""
/admins

/documentacion

/comandos

/sum {num} {num}

/rest {num} {num}

/div {num} {num}

/multi {num} {num}

/clima {ciudad}
""")

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
  suma = numOne + numTwo
  await ctx.send("La suma da "+ str(suma))

@bot.command()
async def multi(ctx, numOne: int, numTwo: int):
  multiplicacion = numOne * numTwo
  await ctx.send("La multiplicacion da "+ str(multiplicacion))

@bot.command()
async def div(ctx, numOne: int, numTwo: int):
  division = numOne / numTwo
  await ctx.send("La division da "+ str(division))

@bot.command()
async def rest(ctx, numOne: int, numTwo: int):
  resta = numOne - numTwo
  await ctx.send("La resta da "+ str(resta))

@bot.command()
async def tuki(ctx):
  await ctx.send("TUKI SEÑAL")

@bot.command()
async def clima(ctx, ciudad:str):
  response = session.get(f'https://www.google.com/search?q=el+clima+ {ciudad}&rlz=1C1ONGR_esAR1008AR1008&oq=el+clima+{ciudad}&aqs=chrome.0.0i512j0i22i30l9.10551j1j7&sourceid=chrome&ie=UTF-8')
  
  soup = BeautifulSoup(response.content, 'html.parser')

  weather = soup.find('span', {'id': 'wob_dc'}).text
  primary_text = weather
  gs = goslate.Goslate() 
  translated = gs.translate(primary_text, 'es') 
  await ctx.send("El clima en la ciudad de " + ciudad + " es " + translated.lower())


KeepAlive.keep_alive()
bot.run("TOKEN")
