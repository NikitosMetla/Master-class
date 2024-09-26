import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot_token = ""
bot = Bot(token=bot_token, parse_mode="html")
storage_bot = MemoryStorage()
router = Router()


# Хендлер для команды /start
@router.message(F.text == "/start")
async def send_welcome(message: Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Нажми на меня", callback_data="tap_to_me"))
    await message.reply(text="Привет! Я твой бот. Введи /help, чтобы узнать больше.",
                        reply_markup=keyboard.as_markup())

@router.callback_query(F.data == "tap_to_me")
async def send_welcome(call: CallbackQuery):
    await call.message.reply(text="Ты нажал на кнопку")
    await call.message.delete()

# Хендлер для команды /help
@router.message(F.text == "/help")
async def send_help(message: Message):
    help_text = ("Вот список команд, которые ты можешь использовать:\n"
                 "/start - начать работу с ботом\n"
                 "/help - получить помощь")
    await message.reply(help_text)

# Хендлер для текстовых сообщений
@router.message(F.text)
async def echo_message(message: Message):
    await message.reply(f"Ты написал: {message.text}")

@router.message(F.photo)
async def echo_message(message: Message):
    photo = message.photo[-1].file_id
    await message.reply_photo(caption=f"Ты прислал вот такую фотографию",
                              photo=photo)


async def main():
    print(await bot.get_me())
    await bot.delete_webhook(drop_pending_updates=True)
    dp = Dispatcher(storage=storage_bot)
    dp.include_routers(router)
    await dp.start_polling(bot)

asyncio.run(main())
