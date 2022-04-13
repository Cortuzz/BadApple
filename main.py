import sys
import fpstimer

from converters import *


VIDEO_PATH = 'BadApple.mp4'

frame_size = 150
frame_time = 0.01


def play_video(last_frame):
    timer = fpstimer.FPSTimer(30)
    start_frame = 1

    for frame_number in range(start_frame, last_frame - 1):
        sys.stdout.write("\r" + chars[frame_number])
        timer.sleep()

    sys.stdout.write('\n')


if __name__ == '__main__':
    play_video(get_ascii(VIDEO_PATH, frame_size))
