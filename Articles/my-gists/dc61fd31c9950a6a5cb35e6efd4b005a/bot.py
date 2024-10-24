import discord
from discord.ext import commands
import pyotp
import os
import babel

DISCORD_TOKEN = os.environ('DISCORD_TOKEN')
DISCORD_USER_ID  = '233576663533748225'
TELEGRAM_USER_ID  = 'ad3ro1'
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
otp_secret = pyotp.random_base32()

class Bot:
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.command()
    async def lang(ctx):
        available_langs = babel.langs_all()
        selected_lang = 'en'
        message = f'''Language you selected : {selected_lang}'''
        await ctx.send(message)
    @bot.command()
    async def otp(ctx):
        totp = pyotp.TOTP(otp_secret)
        one_time_code = totp.now() 
        message = f"ワンタイムコード: {one_time_code}"
        await ctx.send(message)

    @bot.command()
    async def buy(ctx):
        license_key = gen_license()
        message = f'''Successfully complete! Your license key: {license_key}'''
        await ctx.send(message)

    @bot.command()
    async def contact(ctx):
        contact_info = f'''
        Discord: https://discord.com/users/{DISCORD_USER_ID}
        Telegram: https://t.me/{TELEGRAM_USER_ID}
        '''
        message = f'''ご不明な点がございましたら、お気軽にお問い合わせください。{}'''
        await ctx.send(message)

    @bot.command()
    async def help(ctx):
        help_info =  '''
        OTP自動発行(Bot) チャンネルへようこそ。こちらでは、簡単なコマンド入力によってワンタイムコードなどを手軽に生成できます。
        このチャンネルを活用して、目的の認証を行ってください。

        /lang - 表示言語を選択するにはこちら。
        /otp - ワンタイムコードを取得するにはこちら。
        /buy - 有料ライセンスの購入手続きはこちらから。
        /contact - ご質問やお問い合わせがある場合はこちらから。
        /help - 操作方法やその他情報を表示します。
        '''
        message = help_info
        await ctx.send(message)

bot.run(DISCORD_TOKEN)

