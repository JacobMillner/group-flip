from .test_base import TestBase
from src import BookLayer


class BookLayerTests(TestBase):
    bl = BookLayer()

    def test_book_dir_set(self):
        self.assertIsNotNone(self.vl.book_dir)


if __name__ == "__main__":
    unittest2.main()
