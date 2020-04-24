import os
import os.path
import cv2
from loguru import logger
#from ..models import VidFrame


class ImageUtils():

    # get array of all book folders in dir
    def get_book_dirs(self, dir):
        book_dirs = []
        for folder in os.listdir(dir):
            if os.path.isdir(os.path.join(dir, folder)):
                book_dirs.append(folder)
        return book_dirs

    # get array of image paths in dir
    def get_book_frames(self, book_dir):
        frame_paths = []
        valid_types = os.environ["VALID_FILE_TYPES"]
        valid_types = valid_types.split(",")
        for file in os.listdir(book_dir):
            ext = os.path.splitext(file)[1].strip(".")
            if ext.lower() not in valid_types:
                continue
            frame_paths.append(os.path.join(book_dir, file))
        return frame_paths

    # load individual frame
    # https://stackoverflow.com/questions/40928205/python-opencv-image-to-byte-string-for-json-transfer
    def get_frame_image(self, book_dir, frame):
        img = cv2.imread(book_dir + frame)
        return img
