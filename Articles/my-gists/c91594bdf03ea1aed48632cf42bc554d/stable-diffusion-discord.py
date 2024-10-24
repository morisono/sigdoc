import discord
from discord.ext import commands
from PIL import Image
import requests
from io import BytesIO

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

last_payload = None

@bot.event
async def on_ready():
    print('Ready!')

@bot.event
async def on_message(message):
    global last_payload

    if bot.user.mentioned_in(message) and not message.author.bot:
        payload = None
        prompt = message.content.replace(re.compile(r'<@!?[0-9]+>'), '').strip().replace(re.compile(r'<@&[0-9]+>'), '').strip()

        if len(message.attachments) > 0:
            image_attachment = message.attachments[0]
            image_url = image_attachment.url
            image_response = requests.get(image_url)
            image_buffer = BytesIO(image_response.content)

            image = Image.open(image_buffer)
            width, height = image.size
            print(f'Image Size: {width}x{height}')

            payload = {
                'prompt': prompt,
                'negative_prompt': 'EasyNegativeV2',
                'init_images': [image_buffer.read().decode('base64')],
                'steps': 30,
                'cfg_scale': 7,
                'denoising_strength': 0.5,
                'width': width,
                'height': height
            }
        elif prompt.lower() == 'retry' and last_payload:
            payload = last_payload
            payload['seed'] = -1
        else:
            payload = {
                'prompt': prompt,
                'negative_prompt': 'EasyNegativeV2',
                'steps': 30,
                'cfg_scale': 7,
                'width': 640,
                'height': 960
            }

        try:
            api_url = 'http://XXX.X.X.X:XXXX/sdapi/v1/img2img' if payload.get('init_images') else 'http://127.0.0.1:7860/sdapi/v1/txt2img'
            api_response = requests.post(api_url, json=payload, headers={'Content-Type': 'application/json'})
            api_data = api_response.json()
            last_payload = payload

            if 'images' in api_data and len(api_data['images']) > 0:
                output_image_buffer = BytesIO(api_data['images'][0].encode('base64'))
                await message.reply(file=discord.File(output_image_buffer, filename='output.png'))
            else:
                await message.reply('Failed to generate image.')
        except Exception as error:
            print('Error during API request:', error)
            await message.reply(f'Error during API request: {error}')

bot.run('YourBotToken')
