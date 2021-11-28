FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install pyTelegramBotAPI numpy Pillow opencv-python-headless pytube

ADD YoutubeGifBot.py /
CMD [ "python3", "./YoutubeGifBot.py" ]