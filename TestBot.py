# -*- coding: utf-8 -*-
import telebot
from random import randint
from PIL import Image


bot = telebot.TeleBot('1289161819:AAE17tjr5fHS8Gzh9gOLthnl4kfv476irOk');
img = Image.open("KU3NiiWx58M.png")
stck = {"happy":"CAACAgIAAxkBAAEBcKFfgL6cxF53Iv5jjlRS9VGJVEveHAAChgIAAladvQrq5guSx3G2ARsE",
            "angry":"CAACAgIAAxkBAAEBcKlfgL_t1tUi-IP89rXSA-YQaU_MTwACZwUAAj-VzAoofuUG7r451BsE",
            "sad":"CAACAgIAAxkBAAEBcOxfgTuA-giM37R5lqw9yzjZ4K-kjgACGwADO2AkFNCUnNAljlGHGwQ",
            "cool":"CAACAgIAAxkBAAEBcKNfgL78kt8ZrVEXIh8edvUamqk56AACRgADWbv8JRLr_Wbcq939GwQ",
            "ok":"CAACAgIAAxkBAAEBcKtfgMAtq6QgNuZ8evYnXdNaNwABrX4AArABAAJWnb0Kkxj0i04olskbBA"}
att = 0
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global att
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет тебе, друг!")
        att = 0
    elif message.text == "/start":
        bot.send_message(message.chat.id, "Привет!\nМои команды:\n - Привет\n - Напиши [сообщение]\n - /help\n - Переверни [сообщение]\n - Отправь фото\n - Отправь стикер")
        att = 0
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Мои команды:\n - Привет\n - Напиши [сообщение]\n - /help\n - Переверни [сообщение]\n - Отправь фото\n - Отправь стикер")
        att = 0
    elif "переверни" in message.text.lower():
        words = str(message.text[9:])
        bot.send_message(message.chat.id, words[::-1])
        att = 0
    elif "напиши" in message.text.lower():
        words = str(message.text[7:])
        bot.send_message(message.chat.id, words)
        att = 0
    elif message.text.lower() == "отправь фото":
        bot.send_photo(message.chat.id, img)
        att = 0
    elif message.text.lower() == "отправь стикер":
        bot.send_sticker(message.chat.id, stck["ok"])
        att = 0
    else: 
        print(att)
        if att < 4:
            bot.send_message(message.chat.id, "Извини, я тебя не понимаю")
            bot.send_sticker(message.chat.id, stck["sad"])
            att+=1
        else: 
            if att < 6:
                bot.send_message(message.chat.id, "Перестань так делать!!")
                bot.send_sticker(message.chat.id, "CAACAgEAAxkBAAEBcRJfgZKQeSPJXb9C9zPh_GA8xTjJVQAC4gADOA6CEeTgk4YIcTeWGwQ")
                att+=1
            else:
                bot.send_sticker(message.chat.id, stck["angry"])
    name = message.from_user.first_name
    print(message.from_user)
    print("[{0}]: {1}".format(name, message.text))
bot.polling(none_stop=True, interval=0.01)