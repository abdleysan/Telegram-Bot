import requests
import time
import random
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN: str = '<bot token>'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Приветствую, я магический шар!\n И я знаю ответ на любой твой вопрос.')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer('Задайте мне интересующий Вас вопрос.')

# Этот хэндлер будет срабатывать на команду "/question"
@dp.message_handler(commands=['question'])
async def process_question_command(message: types.Message):
    await message.answer('Введите интересующий Вас вопрос:')    


@dp.message_handler()
async def send_echo(message: types.Message):
    answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да','Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    await message.reply(random.choice(answers))

dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')

dp.register_message_handler(send_echo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)