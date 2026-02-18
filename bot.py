import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = "https://flbar.ru"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[[
            types.KeyboardButton(
                text="🌸 Открыть каталог букетов",
                web_app=types.WebAppInfo(url=WEBAPP_URL)
            )
        ]],
        resize_keyboard=True
    )
    await message.answer(
        "Нажмите кнопку, чтобы открыть каталог букетов",
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
