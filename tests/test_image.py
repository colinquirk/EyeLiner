import os
import unittest

import eyeliner


class TestImage(unittest.TestCase):

    def test_image_creation(self):
        img = eyeliner.Image()
        self.assertEqual(img.out_size, 224)
        self.assertEqual(img.screen_width, 1920)
        self.assertEqual(img.screen_height, 1080)

        img2 = eyeliner.Image(out_size=500, screen_width=1600, screen_height=1200)
        self.assertEqual(img2.out_size, 500)
        self.assertEqual(img2.screen_width, 1600)
        self.assertEqual(img2.screen_height, 1200)

    def test_image_draw(self):
        img = eyeliner.Image()
        points = [(960, 540), (20, 20), (20, 1060), (1900, 1060), (1900, 20), (960, 540)]

        img.draw(points)

        with self.assertRaises(TypeError):
            img.draw(100)

        with self.assertRaises(TypeError):
            img.draw("100")

        with self.assertRaises(TypeError):
            img.draw({'test': 100})

    def test_image_output(self):
        fname = 'test.png'
        try:
            os.remove(fname)
        except FileNotFoundError:
            pass

        img = eyeliner.Image()
        points = [(960, 540), (20, 20), (20, 1060), (1900, 1060), (1900, 20), (960, 540)]
        img.draw(points)
        img.write(fname)

        self.assertTrue(os.path.exists(fname))