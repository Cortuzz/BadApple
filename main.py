import sys
import fpstimer
from pygame import mixer

from converters import *


VIDEO_PATH = 'BadApple.mp4'

frame_size = 100
frame_time = 0.01


def play_audio(path):
    mixer.pre_init(44100, -16, 2, 2048)
    mixer.init()
    mixer.music.load(path)
    mixer.music.set_volume(1)
    mixer.music.play()


def play_video(last_frame):
    timer = fpstimer.FPSTimer(30)
    start_frame = 1

    for frame_number in range(start_frame, last_frame - 1):
        sys.stdout.write("\r" + chars[frame_number])
        timer.sleep()

    sys.stdout.write('\n')


if __name__ == '__main__':
    ASCII = get_ascii(VIDEO_PATH, frame_size)
    play_audio("BadApple.mp3")
    play_video(ASCII)
