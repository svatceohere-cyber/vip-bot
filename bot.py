from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
import asyncio

TOKEN = "8901833217:AAFR-2y7jV6vjwDBYAyCqLhkVFo199y4WyI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Головне меню
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚀 Розпочати")]
    ],
    resize_keyboard=True
)

# Меню доступу
access_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎁 Безкоштовний доступ")],
        [KeyboardButton(text="💎 Купити доступ")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

# Меню безкоштовного доступу
free_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔗 Реєстрація")],
        [KeyboardButton(text="🆔 Надіслати ID")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Вітаємо!\n\n"
        "Ласкаво просимо до офіційного переходника у VIP Клуб.\n\n"
        "Учасники клубу отримують:\n"
        "📈 Аналітику ринку\n"
        "🎯 Торгові рекомендації\n"
        "🔥 Ексклюзивний контент\n"
        "💬 Закрите ком'юніті трейдерів\n\n"
        "Натисніть «🚀 Розпочати».",
        reply_markup=start_keyboard
    )

@dp.message(F.text == "🚀 Розпочати")
async def begin(message: Message):
    await message.answer(
        "Оберіть спосіб отримання доступу:",
        reply_markup=access_keyboard
    )

@dp.message(F.text == "🎁 Безкоштовний доступ")
async def free_access(message: Message):
    await message.answer(
        "🎁 VIP БЕЗКОШТОВНО\n\n"
        "Для отримання доступу:\n\n"
        "1️⃣ Зареєструйтесь за реферальним посиланням.\n"
        "2️⃣ Надішліть свій ID.\n"
        "3️⃣ Поповніть баланс мінімум на 10$.\n"
        "4️⃣ Отримайте доступ до VIP Клубу.",
        reply_markup=free_keyboard
    )

@dp.message(F.text == "💎 Купити доступ")
async def paid_access(message: Message):
    await message.answer(
        "💎 Купівля доступу\n\n"
        "Незабаром тут буде вибір способу оплати."
    )

@dp.message(F.text == "🔗 Реєстрація")
async def registration(message: Message):
    await message.answer(
        "Ваше реферальне посилання:\n\n"
        "ТУТ_БУДЕ_ПОСИЛАННЯ"
    )

@dp.message(F.text == "🆔 Надіслати ID")
async def send_id(message: Message):
    await message.answer(
        "Надішліть ваш Pocket Option ID одним повідомленням."
    )

@dp.message(F.text == "⬅️ Назад")
async def back(message: Message):
    await message.answer(
        "Повернення до головного меню.",
        reply_markup=start_keyboard
    )

async def main():
    print("Бот запущений")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())