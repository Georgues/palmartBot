from aiogram import executor
from dispatcher import dp
from handlers import callbacks
from handlers import personal_actions
from handlers import parser
from datetime import datetime
import config


if __name__ == "__main__":
    config.last_time = datetime.now()
    executor.start_polling(dp, skip_updates=True)
