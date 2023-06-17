import telebot
from telebot import types
from button_calback import callback


bot = telebot.TeleBot("")

user_info = {}


@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    user_info["id"] = message.from_user.id,
    user_info["name"] = message.from_user.first_name

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_refuge = types.KeyboardButton("Убежище")
    button_visa = types.KeyboardButton("Виза в США")
    button_other = types.KeyboardButton("Другое")
    markup.add(button_refuge, button_visa, button_other)

    bot.send_message(message.chat.id, f"Hello, {user_info['name']}!\nЕсли вам нужна помощь иммиграционного эксперта, выберите, пожалуйста, или напишите, что именно Вас интересует:", reply_markup=markup)
    print(message.chat.id)


@bot.message_handler(content_types=["text"])
def send_info_button(message):
    # попробовать придумать оптимизацию кода, в плане читабельности
    inline_markup_1 = types.InlineKeyboardMarkup(row_width=1)
    button_main_1 = types.InlineKeyboardButton("Получить консультацию", callback_data="main_1")
    inline_markup_1.add(button_main_1)

    inline_markup_2 = types.InlineKeyboardMarkup(row_width=1)
    button_main_2 = types.InlineKeyboardButton("Получить консультацию", callback_data="main_2")
    inline_markup_2.add(button_main_2)

    inline_markup_3 = types.InlineKeyboardMarkup(row_width=1)
    button_main_3 = types.InlineKeyboardButton("Получить консультацию", callback_data="main_3")
    inline_markup_3.add(button_main_3)


    if message.text == "Убежище": #проработать возможность упрощения кода в виде читабельность без потери скорости и без роста памяти
        bot.send_message(message.chat.id, callback(message.text), reply_markup=inline_markup_1)

    elif message.text == "Виза в США":
        bot.send_message(message.chat.id, callback(message.text), reply_markup=inline_markup_2)

    elif message.text == "Другое":
        bot.send_message(message.chat.id, callback(message.text), reply_markup=inline_markup_3)


@bot.callback_query_handler(func=lambda call: True)

def step(call):

    username = f"@{call.from_user.username}" # попробовать придумать оптимизацию кода, в плане читабельности
    user_id = f"tg://user?id={call.from_user.id}"


    if call.data == "main_1":
        bot.send_message(call.message.chat.id, "Спасибо, что вы решились записаться на консультацию.\nНаш юрист свяжется с вами в ближайшее время!")
        bot.send_message(-920363299, f"Убежище - {username}, {user_id}")

    elif call.data == "main_2":
        bot.send_message(call.message.chat.id, "Спасибо, что вы решились записаться на консультацию.\nНаш юрист свяжется с вами в ближайшее время!")
        bot.send_message(-920363299, f"Виза в США - {username}, {user_id}")

    elif call.data == "main_3":
        bot.send_message(call.message.chat.id, "Спасибо, что вы решились записаться на консультацию.\nНаш юрист свяжется с вами в ближайшее время!")
        bot.send_message(-920363299, f"Другое - {username}, {user_id}")


bot.infinity_polling()

