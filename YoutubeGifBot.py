import telebot
import time
from GIF import GIF

bot = telebot.TeleBot('2125057771:AAHzoKqLjbtho2kQuxy8evJV07q4dvkB3Eg')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    gif = GIF()
    if message.text[:4] == "http" and len(message.text) > 10:
        try:
            split_space = str(message.text).split(' ')
            filename, cut_frames, color = gif.downloadVideo(split_space)
            gif.createGIF(split_space, filename, cut_frames, color)

            with open(gif.path + filename + '.gif', 'rb') as f1:
                bot.send_animation(message.from_user.id, f1)

            time.sleep(2)
            gif.remove(filename)
        except UnicodeError:
            bot.send_message(message.from_user.id, "Invalid input")
            try:
                gif.remove(filename)
            except Exception:
                pass
    else:
        bot.send_message(message.from_user.id, "Я могу только делать гифки, так что дай ссылку "
                                               "и 2 тайстемпа в виде 'link mm:ss mm:ss'."
                                               "\nТакже можешь добавить 2 значения - деление кадров "
                                               "и цвет. \nДеление: 1 - по умолчанию фулл кадры, 2 - "
                                               "берем половину кадров из потока, 3 - треть, и т.д."
                                               "\nЦвет: 1 - по умолчанию, 2 - gray"
                                               "\n\nЧем больше деление, тем хуже восприятие картинки, "
                                               "так как она будет двигаться рывками. Такое рекомендуется "
                                               "использовать на большом промежутке времени, чтобы Телеграм "
                                               "смог отправить гифку большого объема. Например, гифка 1 секунды "
                                               "с полными кадрами весит 2,5 МБ, так что Телеграм не сможет принять "
                                               "гифку длиннее +-20 секунд, да и он её долго обрабатывать будет")

bot.polling(none_stop=True, interval=0)
