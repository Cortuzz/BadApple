import cv2
from PIL import Image

REVERSING = True
brightness_chars = ["#", "Σ", "S", "%", "?", "*", "+", ";", ":", ",", " "]

if REVERSING:
    brightness_chars.reverse()

chars = []


def convert_to_ascii(image_frame):
    pixels = image_frame.getdata()
    characters = "".join([brightness_chars[pixel // 25] for pixel in pixels])

    return characters


def get_ascii(path, size):
    video = cv2.VideoCapture(path)

    frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video.release()
    parse(path, frames, size)

    return frames


def parse(path, frames, size):
    capture = cv2.VideoCapture(path)
    capture.set(1, 0)
    frame = 1

    while frame <= frames:
        read, image_frame = capture.read()
        if not read:
            break

        image = Image.fromarray(image_frame)
        ascii_characters = convert_to_ascii(rgb_to_sepia(resize_image(image, size)))
        pixel_count = len(ascii_characters)
        ascii_image = "\n".join(
            [ascii_characters[index:(index + size)] for index in range(0, pixel_count, size)])

        chars.append(ascii_image)
        frame += 1

    capture.release()


def rgb_to_sepia(image_frame):
    return image_frame.convert("L")


def resize_image(image, size):
    width, height = image.size
    ratio = (height / float(width * 2.5))

    new_height = int(ratio * size)
    resized_image = image.resize((size, new_height))

    return resized_image
