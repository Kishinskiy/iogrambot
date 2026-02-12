from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboard as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        text=f"Welcome!, {message.from_user.full_name}",
        reply_markup=kb.second
    )

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('команда помощи /help')


@router.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer('OK!')


@router.message(F.photo)
async def send_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo="https://picsum.photos/200", caption="случайное изображение")

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Hello!', reply_markup=await kb.start_keyboard())
