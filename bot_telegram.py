from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handlers(commands=['help'])
async def echo_send(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp)
