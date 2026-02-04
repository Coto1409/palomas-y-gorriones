import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
#Crear un bot de discord que clasifique imagenes
@bot.command()
async def classify_image(ctx, image_url: str):
    # Aquí iría la lógica para clasificar la imagen usando un modelo preentrenado
    # Por simplicidad, vamos a simular una clasificación
    classification = "Esta imagen es un gato."  # Simulación de clasificación
    await ctx.send(f'Clasificación de la imagen: {classification}')
bot.run("TOKEN")