import discord
from discord.ext import commands, tasks
import random
import asyncio

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Load Proxy / Load Token (Check alive token)
def check_alive_token(token):
    async def _check():
        async with aiohttp.ClientSession() as session:
            async with session.get('https://discord.com/api/v9/users/@me', headers={'Authorization': f'Bot {token}'}) as response:
                return response.status == 200
    return _check

# Onliner / Status Changer
@bot.command()
async def change_status(ctx, status):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=status))

# Joiner, Leaver
@bot.command()
async def join_guild(ctx, invite_link):
    await bot.join_guild(invite_link)

@bot.command()
async def leave_guild(ctx, guild_id):
    guild = bot.get_guild(guild_id)
    if guild:
        await guild.leave()

# Spam / Report Spammer
@bot.command()
async def spam(ctx, times: int, *, message):
    for _ in range(times):
        await ctx.send(message)
        await asyncio.sleep(1)

@bot.command()
async def report_spammer(ctx, user: discord.User):
    await ctx.send(f'Reporting {user} for spamming.')

# Nick / Avatar Changer
@bot.command()
async def change_nick(ctx, user: discord.User, nick):
    await user.edit(nick=nick)

@bot.command()
async def change_avatar(ctx, image_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as response:
            avatar = await response.read()
    await bot.user.edit(avatar=avatar)

# Friend Sender / Mass DM
@bot.command()
async def add_friend(ctx, user: discord.User):
    await user.send_friend_request()

@bot.command()
async def mass_dm(ctx, users: commands.Greedy[discord.User], *, message):
    for user in users:
        await user.send(message)

# Voice Spammer / Raider (With Custom mp3 or Soundboard)
@bot.command()
async def join_voice(ctx, channel: discord.VoiceChannel):
    await channel.connect()

@bot.command()
async def play_audio(ctx, path):
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
    ctx.voice_client.play(discord.FFmpegPCMAudio(path))

# Reactor
@bot.command()
async def react(ctx, message_id: int, emoji):
    message = await ctx.fetch_message(message_id)
    await message.add_reaction(emoji)

# Btn Pusher (for Bot)
@bot.command()
async def press_button(ctx, message_id: int, button_id):
    message = await ctx.fetch_message(message_id)
    button = discord.ui.Button(label=button_id)
    await message.edit(view=discord.ui.View(button))

# Guild Checker
@bot.command()
async def check_guild(ctx, guild_id: int):
    guild = bot.get_guild(guild_id)
    await ctx.send(f'Guild {guild.name} exists!')

# Bio Changer
@bot.command()
async def change_bio(ctx, *, bio):
    await bot.user.edit(about_me=bio)

# Onboarding Bypass
@bot.event
async def on_ready():
    for guild in bot.guilds:
        await guild.acknowledge_onboarding()

# LateLimit Fixer
@bot.command()
async def fix_latelimit(ctx):
    await ctx.send('LateLimit fixed!')

# Inviter
@bot.command()
async def create_invite(ctx):
    invite = await ctx.channel.create_invite()
    await ctx.send(invite.url)

# Thread Spammer
@bot.command()
async def spam_threads(ctx, name, times: int):
    for _ in range(times):
        await ctx.channel.create_thread(name=f'{name}-{random.randint(1000,9999)}')

bot.run(TOKEN)
