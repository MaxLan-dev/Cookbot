# import openai
# from aiogram import Bot, Dispatcher, executor, types
# import config
# import logging

# messages = []

# hstr = open('h.txt', 'a')

# CHANNEL_ID = "-1001902525507"


# dispatcher = Dispatcher(bot)

import logging
#from os import environ as env
#from dotenv import load_dotenv

import telebot
import openai
#openai.api_key = "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"
#bot = Bot(token="6619295811:AAHobjQDD1uLuRMhNS6CeeMZtrfJs4ZRPt4")

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

#load_dotenv()
bot = telebot.TeleBot("6619295811:AAHobjQDD1uLuRMhNS6CeeMZtrfJs4ZRPt4")
openai.api_key = "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"
#user_id = int(env["USER_KEY"])


@bot.message_handler(func=lambda message: True)
def get_response(message):
#   if int(message.chat.id) != user_id:
#     bot.send_message("This bot is not for public but private use only.")
#   else:
    response = ""
    if message.text.startswith(">>>"):
      # Use Codex API for code completion
      response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=f'```\n{message.text[3:]}\n```',
        temperature=0,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n", ">>>"],
      )
    else:
      # Use GPT API for text completion
      # Check if the question is about code or not
      if "code" in message.text.lower() or "python" in message.text.lower():
        # Use Codex API for code-related questions
        response = openai.Completion.create(
          engine="code-davinci-002",
          prompt=f'"""\n{message.text}\n"""',
          temperature=0,
          max_tokens=4000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          stop=['"""'],
        )
      else:
        # Use GPT API for non-code-related questions
        response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=f'"""\n{message.text}\n"""',
          temperature=0,
          max_tokens=2000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          stop=['"""'],
        )

    bot.send_message(message.chat.id, f'{response["choices"][0]["text"]}', parse_mode="None")

bot.infinity_polling()
# @dispatcher.message_handler(commands=['start'])
# async def start(message: types.Message):
#     user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

#     if user_channel_status['status'] != 'left':
#         await bot.send_message(message.from_user.id, "Спасибо за подписку на канал! ChatGPT 3.5 готов к работе!")
#     else:
#         button = types.InlineKeyboardButton("Я подписался", callback_data="Я подписался")
#         markup = types.InlineKeyboardMarkup(row_width=1).add(button)

#         await bot.send_message(message.from_user.id, "Сначала подпишись на канал! https://t.me/shinkarukdev", reply_markup=markup)


# @dispatcher.callback_query_handler(lambda call: True)
# async def callback(call: types.CallbackQuery):
#     if call.message:
#         user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)

#         if user_channel_status["status"] != "left":
#             await bot.send_message(call.from_user.id, "Спасибо за подписку!")
#         else:
#             await bot.send_message(call.from_user.id, "Вы не подписались :(")


# def chatgpt(message):
#     messages.append({"role": "user", "content": message})
#     chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
#     reply = chat.choices[0].message.content
#     messages.append({"role": "assistant", "content": reply})
#     return reply



# @dispatcher.message_handler()
# async def f(message):
#     user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

#     if message.text[0] != '/' and user_channel_status["status"] != "left":
#         hstr.write(message.text)
#         hstr.write('\n')
#         await bot.send_message(message.chat.id, 'ChatGPT набирает сообщение...')
#         await bot.send_message(message.chat.id, chatgpt(message.text))
#     else:
#         await bot.send_message(message.chat.id, 'ChatGPT ждет подписки на канал https://t.me/shinkarukdev')


# #hstr.close()


# if __name__ == '__main__':
#     executor.start_polling(dispatcher)
