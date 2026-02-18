import asyncio
import os
import json
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USERNAME = "mariakrusty"
WEBAPP_URL = "https://mariakrusty.github.io/tg-flbar-bot/webapp/index.html"

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
        "Мы — не цветочная мастерская.\n"
        "Мы — портал в состояние душевного дома.\n\n"
        "Нажмите кнопку, чтобы открыть каталог букетов к 8 марта 🌸",
        reply_markup=kb
    )

@dp.message(F.web_app_data)
async def handle_order(message: types.Message):
    data = json.loads(message.web_app_data.data)
    name = data.get("name")
    price = data.get("price")
    user = message.from_user
    username = f"@{user.username}" if user.username else user.full_name

    await message.answer(
        f"✅ Ваш заказ принят!\n\n"
        f"💐 {name}\n"
        f"💰 {price:,} ₽\n\n"
        f"Мы свяжемся с вами в ближайшее время."
    )

    await bot.send_message(
        chat_id=f"@{ADMIN_USERNAME}",
        text=f"🛍 Новый заказ!\n\n"
             f"👤 Клиент: {username}\n"
             f"💐 Букет: {name}\n"
             f"💰 Сумма: {price:,} ₽"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
