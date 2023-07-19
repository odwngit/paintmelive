import nextcord
from nextcord.ext import commands
import config
import time
import paint
import json

pnt = paint.Painter()
pnt.clear(200, 200)
pnt.saveImage()

# boilerplate
intents = nextcord.Intents.all()
intents.members = True

# prefix definition
bot = commands.Bot(command_prefix="$", intents=intents)

#bot login
@bot.event
async def on_ready():
    print(f"logged in as {bot.user.name}, {bot.user.id}")
#bot commands
@bot.command()
async def helpme(ctx):
    await ctx.send("Do `$paint x y color` where `color` is one of these:")
    await ctx.send("- red")
    await ctx.send("- orange")
    await ctx.send("- yellow")
    await ctx.send("- green")
    await ctx.send("- blue")
    await ctx.send("- purple")
    await ctx.send("- black")

@bot.command()
async def paint(ctx, x, y, c):
    pnt.set(int(x), int(y), pnt.convert(c))
    print("saving image...")
    pnt.saveImage()
    with open("out/blackup.json", "w") as f:
        json.dump(pnt.pixels, f)

bot.run(config.token)