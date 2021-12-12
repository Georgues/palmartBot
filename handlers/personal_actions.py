from aiogram import types
from dispatcher import dp
from handlers.parser import getData


@dp.message_handler(commands=["getId"])
async def return_id_command(message: types.Message):
    await message.answer(message.from_user.id)


@dp.message_handler(commands=["getOrders"])
async def return_id_command(message: types.Message):
    await message.answer(getData())
