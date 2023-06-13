import telebot
from telebot import types


bot = telebot.TeleBot("TOKEN")

user_info = {}

@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    user_info["id"] = message.from_user.id,
    user_info["name"] = message.from_user.first_name

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_refuge = types.KeyboardButton("Политическое убежище")
    button_visa = types.KeyboardButton("Виза в США")
    button_lawyer = types.KeyboardButton("Адвокат в США")
    button_other = types.KeyboardButton("Другое")


    markup.add(button_refuge, button_visa, button_lawyer, button_other)

    bot.send_message(message.chat.id, f"Hello, {user_info['name']}!\nЕсли вам нужна помощь иммиграционного эксперта, выберите, пожалуйста, или напишите, что именно Вас интересует:", reply_markup=markup)


main_dict = {
    "Политическое убежище": [],
    "Виза в США": [],
    "Адвокат в США": [],
    "Другое": []
}
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

    inline_markup_4 = types.InlineKeyboardMarkup(row_width=1)
    button_main_4 = types.InlineKeyboardButton("Получить консультацию", callback_data="main_4")
    inline_markup_4.add(button_main_4)

    if message.text == "Политическое убежище": #проработать возможность упрощения кода в виде читабельность без потери скорости и без роста памяти
        bot.send_message(message.chat.id, """
Мы готовы предоставить Вам консультацию по вопросам политического убежища.
Чтобы записаться, вам нужно просто нажать на кнопку.
Далее, наш юрист свяжется с Вами и ответит на все интересующие Вас вопросы!
        """, reply_markup=inline_markup_1)



    elif message.text == "Виза в США":
        bot.send_message(message.chat.id, """
Мы готовы предоставить Вам консультацию по вопросам получения визы в США.
Наши юристы работают по всем видам виз (бизнес, рабочие, студенческие). Чтобы записаться,
просто нажмите на кнопку. Наш юрист свяжется с Вами в ближайшее время, ознакомится с вашим запросом и ответит на все интересующие Вас вопросы
        """, reply_markup=inline_markup_2)

    elif message.text == "Другое":
        bot.send_message(message.chat.id, "Мы готовы предоставить Вам консультацию по интересующему вас вопросу. Чтобы записаться, просто нажмите на кнопку. Наш юрист свяжется с Вами в ближайшее время, ознакомится с вашим запросом и ответит на все интересующие Вас вопросы", reply_markup=inline_markup_3)


@bot.callback_query_handler(func=lambda call: True)
def step(call):
    username = f"@{call.from_user.username}" # попробовать придумать оптимизацию кода, в плане читабельности
    if call.data == "main_1":
        bot.send_message(call.message.chat.id, "Спасибо, что вы решились записаться на консультацию.\nНаш юрист свяжется с вами в ближайшее время!")
        main_dict["Политическое убежище"].append(username)
    elif call.data == "main_2":
        bot.send_message(call.message.chat.id, "Спасибо, что вы решились записаться на консультацию.\nНаш юрист свяжется с вами в ближайшее время!")
        main_dict["Виза в США"].append(username)
    elif call.data == "main_3":
        bot.send_message(call.message.chat.id, "Спасибо, что вы решились записаться на консультацию.\nНаш юрист свяжется с вами в ближайшее время!")

        main_dict["Другое"].append(username)
    elif call.data == "main_4":
        bot.send_message(call.message.chat.id, "Спасибо, что вы решились записаться на консультацию.\nНаш юрист свяжется с вами в ближайшее время!")














bot.infinity_polling()

