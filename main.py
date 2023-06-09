import telebot
from telebot import types

bot = telebot.TeleBot("6235791340:AAGLY_OjJ-MG_bwFJV0jOC8KktmZnpLe8jQ")

@bot.message_handler(commands=["start"])
def send_welcome_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_one = types.KeyboardButton("Политическое убежище")
    button_two = types.KeyboardButton("Стоимость кон-ии")
    button_three = types.KeyboardButton("Запись на кон-ию")
    button_fouth = types.KeyboardButton("С чего начать?")
    button_five = types.KeyboardButton("Туристическая виза")
    button_six = types.KeyboardButton("Студенческая виза")


    markup.add(
        button_one,
        button_two,
        button_three,
        button_fouth,
        button_five,
        button_six
    )

    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}!\nЕсли вам нужна помощь иммиграционного эксперта, выберите, пожалуйста, или напишите, что именно Вас интересует:", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def send_info_menu(message):


    if message.text == "Запись на кон-ию":
        bot.send_message(message.chat.id, "Расскажите о себе: (возраст, профессия и т.д)")
    if type(message.text) == str:
        txt = message.text
    print(txt)


bot.infinity_polling()

