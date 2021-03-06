import sys
import fpstimer
from pygame import mixer

from converters import *

PATH = 'BadApple'

VIDEO_PATH = '{}.mp4'.format(PATH)
AUDIO_PATH = '{}.mp3'.format(PATH)

MODE = "2K"
frame_time = 0.01


def check_mode(mode):
    if mode is "2K":
        return 212
    elif mode is "FHD":
        return 200
    else:
        raise Exception("Bad mode")


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
    frame_size = check_mode(MODE)
    ASCII = get_ascii(VIDEO_PATH, frame_size)
    play_audio(AUDIO_PATH)
    play_video(ASCII)
