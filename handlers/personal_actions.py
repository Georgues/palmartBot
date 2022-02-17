from aiogram import types
from dispatcher import dp
from handlers.parser import getOrders
from handlers.parser import getOrdersDetailed
from datetime import datetime
import config

# last_time = datetime.now()


@dp.message_handler(commands=["start"])
async def return_id_command(message: types.Message):
    try:
        answer = "Приветствую, Биджо, я бот-темщик, вот че могу и умею: CHANGES\n" \
                 "/help - почитать список команд и прочую поеботу\n" \
                 "/getId - получить id твоего аккаунта (для фильтрации доступа)\n" \
                 "/getOrders - агрегированная информация о заказах на сегодня (сумма+количество)\n" \
                 "/getOrdersDetailed - детализированная информация по заказам\n" \
                 "Пока больше ничего не умею(("
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["/getOrders", "/getOrdersDetailed", "/getId", "/help"]
        keyboard.add(*buttons)
        await message.answer(answer, reply_markup=keyboard)
    except:
        await message.answer("Биджо-бот болеет, если скоро не выздоровеет - чекайте логи")


@dp.message_handler(commands=["getId"])
async def return_id_command(message: types.Message):
    try:
        await message.answer(message.from_user.id)
    except:
        await message.answer("Биджо-бот болеет, если скоро не выздоровеет - чекайте логи")


@dp.message_handler(is_admin=True, commands=["getOrders"])
async def return_id_command(message: types.Message):
    delta = datetime.now() - config.last_time
    if delta.seconds > 5:
        config.last_time = datetime.now()
        try:
            await message.answer(getOrders())
        except:
            await message.answer("Биджо-бот болеет, если скоро не выздоровеет - чекайте логи")
    else:
        try:
            await message.answer("Подождите 5-10 секунд")
        except:
            await message.answer("Биджо-бот болеет, если скоро не выздоровеет - чекайте логи")


@dp.message_handler(is_admin=True, commands=["getOrdersDetailed"])
async def return_id_command(message: types.Message):
    delta = datetime.now() - config.last_time
    if delta.seconds > 5:
        config.last_time = datetime.now()
        try:
            await message.answer(getOrdersDetailed())
        except:
            await message.answer("Биджо-бот болеет, если скоро не выздоровеет - чекайте логи")
    else:
        try:
            await message.answer("Подождите 5-10 секунд")
        except:
            await message.answer("Биджо-бот болеет, если скоро не выздоровеет - чекайте логи")


# @dp.message_handler(is_admin=True, commands=["getCleanJson"])
# async def return_id_command(message: types.Message):
#     try:
#         await message.answer(printJson())
#     except:
#         await message.answer("Биджо-бот болеет, если скоро не выздоровеет - чекайте логи")


@dp.message_handler(commands=["help"])
async def return_id_command(message: types.Message):
    try:
        answer = "Ещё раз привет, походу ты забыл хитровыебанные названия команд, лови список:\n" \
                 "/help - почитать список команд и прочую поеботу\n" \
                 "/getId - получить id твоего аккаунта (для фильтрации доступа)\n" \
                 "/getOrders - агрегированная информация о заказах на сегодня (сумма+количество)\n" \
                 "/getOrdersDetailed - детализированная информация по заказам\n" \
                 "По всем вопросам: @Georgiums"
        await message.answer(answer)
    except:
        await message.answer("Биджо-бот болеет, если скоро не выздоровеет - чекайте логи")
