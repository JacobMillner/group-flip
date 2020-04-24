from tests import TestBase
from utils import ImageUtils


# test data:
# test dir has 2 book folders
# book_1 has 25 frames
# book_2 has 30 frames


class ImageUtilsTests(TestBase):
    iu = ImageUtils()

    def test_get_book_dirs(self):
        test_dir = self.path("test_data/books")
        book_dirs = self.iu.get_book_dirs(test_dir)
        self.assertEqual(len(book_dirs), 2)

    def test_get_book_frames(self):
        vid1_dir = self.path("test_data/books/book_1/")
        vid2_dir = self.path("test_data/books/book_2/")
        vid1_frames = self.iu.get_book_frames(vid1_dir)
        vid2_frames = self.iu.get_book_frames(vid2_dir)
        self.assertEqual(len(vid1_frames), 25)
        self.assertEqual(len(vid2_frames), 30)

    def test_get_book_frame(self):
        frame_to_load_dir = self.path("test_data/books/book_1/")
        frame_to_load = "frame_1.png"
        frame = self.iu.get_frame_image(frame_to_load_dir, frame_to_load)
        # check if cv2 loaded the image
        self.assertIsNotNone(frame)
        self.assertNotEqual(len(frame), 0)


if __name__ == "__main__":
    unittest2.main()
