import unittest
import os
from GIF import GIF

class TestYoutubeGifBot(unittest.TestCase):

    def setUp(self):
        self.gif = GIF()

    def test_download_and_create(self):
        self.assertEqual(self.gif.downloadVideo(['https://www.youtube.com/watch?v=UptDZeIeVOI', '00:03', '00:05', '1', '2']),
                         ('tmp', 1, 2))
        self.assertEqual(self.gif.downloadVideo(['https://www.youtube.com/watch?v=97xf5DXyXqg', '00:37', '00:39']),
                         ('Attack on titan - (Levi Ackerman) -「 AMV 」- Natural', 1, 1))

        self.gif.createGIF(['https://www.youtube.com/watch?v=UptDZeIeVOI', '00:03', '00:05', '1', '2'], 'tmp', 1, 2)
        self.gif.createGIF(['https://www.youtube.com/watch?v=97xf5DXyXqg', '00:37', '00:39'],
                           'Attack on titan - (Levi Ackerman) -「 AMV 」- Natural', 1, 1)

        self.assertTrue(os.path.exists('tmp_soft_eng/tmp.mp4'))
        self.assertTrue(os.path.exists('tmp_soft_eng/tmp.gif'))
        self.assertTrue(os.path.exists('tmp_soft_eng/Attack on titan - (Levi Ackerman) -「 AMV 」- Natural.mp4'))
        self.assertTrue(os.path.exists('tmp_soft_eng/Attack on titan - (Levi Ackerman) -「 AMV 」- Natural.gif'))


if __name__ == '__main__':
    unittest.main()