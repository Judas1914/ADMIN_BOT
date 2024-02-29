import logging
from tools import *
from settings import *

bot.user_data = {
    0: {
        'username': '',
        'first_name': '',
        'mail': '',
        'games': [],
        'market_name': ''
    }
} # Данные пользователей

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
