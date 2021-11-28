import telebot
import getpass
import platform
from pytube import YouTube
import cv2
from PIL import Image
import numpy as np

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
            
            t1 = int(split_space[1].split(':')[0]) * 60 + int(split_space[1].split(':')[1])
            t2 = int(split_space[2].split(':')[0]) * 60 + int(split_space[2].split(':')[1])

            cap = cv2.VideoCapture(path + filename + '.mp4')

            i = 0
            frames = []

            while i <= t2 * 30:
                ret, bgr_frame = cap.read()
                if i >= t1 * 30:
                    if color == 1:
                        frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2RGB)
                    else:
                        frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)
                    frames.append(Image.fromarray(frame))
                i += 1

            cap.release()

            frames[0].save(
                path + filename + '.gif',
                save_all=True,
                append_images=frames[1::cut_frames],
                optimize=True,
                duration=33 * cut_frames,
                loop=0
            )
        except Exception:
            pass
    else:
        bot.send_message(message.from_user.id, 'Напиши \'/help\'')

bot.polling(none_stop=True, interval=0)
