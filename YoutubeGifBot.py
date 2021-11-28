import telebot
import getpass
import platform
from pytube import YouTube

username = getpass.getuser()
my_platform = platform.system()

if my_platform == 'Windows':
    path = 'C:\\Users\\' + username + '\\Downloads\\'
else:
    path = '/home/' + username + '/Загрузки/'

bot = telebot.TeleBot('2125057771:AAHzoKqLjbtho2kQuxy8evJV07q4dvkB3Eg')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global username, my_platform, path
    if message.text[:4] == "http" and len(message.text) > 10:
        try:
            split_space = str(message.text).split(' ')
            yt = YouTube(split_space[0])
            cut_frames = 1
            color = 1
            if len(split_space) > 3:
                cut_frames = int(split_space[3])
                if len(split_space) == 5:
                    color = int(split_space[4])
            filename = yt.title
            yt = yt.streams.get_lowest_resolution()
            yt.download(path, filename=filename + '.mp4')
        except Exception:
            pass
    else:
        bot.send_message(message.from_user.id, 'Напиши \'/help\'')

bot.polling(none_stop=True, interval=0)
