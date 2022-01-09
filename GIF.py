import getpass
import platform
from pytube import YouTube
import cv2
from PIL import Image
import numpy as np
import os


class GIF:
    path = 'tmp_soft_eng/'

    try:
        os.mkdir(path[:-1])
    except:
        pass

    def remove(self, filename):
        os.remove(self.path + filename + '.mp4')
        os.remove(self.path + filename + '.gif')

    def downloadVideo(self, split_space):
        yt = YouTube(split_space[0])
        cut_frames = 1
        color = 1
        if len(split_space) > 3:
            cut_frames = int(split_space[3])
            if len(split_space) == 5:
                color = int(split_space[4])
        filename = yt.title
        yt = yt.streams.get_lowest_resolution()
        try:
            yt.download(self.path, filename=filename + '.mp4')
        except Exception:
            filename = 'tmp'
            yt.download(self.path, filename=filename + '.mp4')
        return filename, cut_frames, color

    def createGIF(self, split_space, filename, cut_frames, color):
        t1 = int(split_space[1].split(':')[0]) * 60 + int(split_space[1].split(':')[1])
        t2 = int(split_space[2].split(':')[0]) * 60 + int(split_space[2].split(':')[1])

        cap = cv2.VideoCapture(self.path + filename + '.mp4')

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
            self.path + filename + '.gif',
            save_all=True,
            append_images=frames[1::cut_frames],
            optimize=True,
            duration=33 * cut_frames,
            loop=0
        )