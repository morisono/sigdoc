from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

# Initialize bot and dispatcher
bot = Bot(token='YOUR_BOT_TOKEN')
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Assuming a dictionary to hold user sessions
user_sessions = {}

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    user_sessions[user_id] = {}  # Initializes or clears the session for the specific user
    await message.reply("Welcome! Your chat history has been cleared.")

@dp.message_handler()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    
    # Retrieve user session, creating a new one if necessary
    session = user_sessions.get(user_id, {})
    
    # Here you would interact with OpenAI API, using the session for context
    # And then update the session with the new message
    
    user_sessions[user_id] = session  # Save the updated session

# More handlers and bot logic here...

if __name__ == '__main__':
    executor.start_polling(dp)