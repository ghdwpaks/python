import discord
from discord.ext import commands

app = commands.Bot(command_prefix='prefix that you want')


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)


app.run('token that you copied')