import telebot

bot = telebot.TeleBot('2125057771:AAHzoKqLjbtho2kQuxy8evJV07q4dvkB3Eg')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши \'Привет\'')
    else:
        bot.send_message(message.from_user.id, 'Напиши \'/help\'')

bot.polling(none_stop=True, interval=0)