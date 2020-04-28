import glob
import os
import unittest

import eyeliner


class TestImage(unittest.TestCase):

    def tearDown(self):
        for f in glob.glob('*.png'):
            os.remove(f)

    def test_image_creation(self):
        img = eyeliner.Image()
        self.assertEqual(img.out_size, 224)
        self.assertEqual(img.screen_width, 1920)
        self.assertEqual(img.screen_height, 1080)

        img2 = eyeliner.Image(out_size=500, screen_width=1600, screen_height=1200)
        self.assertEqual(img2.out_size, 500)
        self.assertEqual(img2.screen_width, 1600)
        self.assertEqual(img2.screen_height, 1200)

    def test_convert_color(self):
        img = eyeliner.Image()
        values = [
            (0.99609375, 0.0, 0.0),
            (0.796875, 0.19921875, 0.0),
            (0.59765625, 0.3984375, 0.0),
            (0.39453125, 0.6015625, 0.0),
            (0.1953125, 0.80078125, 0.0),
            (0.0, 0.99609375, 0.0),
            (0.0, 0.796875, 0.19921875),
            (0.0, 0.59765625, 0.3984375),
            (0.0, 0.39453125, 0.6015625),
            (0.0, 0.1953125, 0.80078125)
        ]

        for i in range(10):
            color = img._calculate_color(i, 10)
            for j, c in enumerate(color):
                self.assertAlmostEqual(c, values[i][j])

    def test_image_draw(self):
        img = eyeliner.Image()
        points = [(960, 540), (20, 20), (20, 1060), (1900, 1060), (1900, 20), (960, 540)]

        img.draw(points)
        img.draw(points, color=True)

        with self.assertRaises(TypeError):
            img.draw(100)

        with self.assertRaises(TypeError):
            img.draw("100")

        with self.assertRaises(TypeError):
            img.draw({'test': 100})

    def test_image_output(self):
        img = eyeliner.Image()
        points = [(960, 540), (20, 20), (20, 1060), (1900, 1060), (1900, 20), (960, 540)]
        img.draw(points)
        img.write('test.png')

        self.assertTrue(os.path.exists('test.png'))

    def test_color_image_output(self):
        img = eyeliner.Image()
        points = [(960, 540), (20, 20), (20, 1060), (1900, 1060), (1900, 20), (960, 540)]
        img.draw(points, color=True)
        img.write('test_color.png')

        self.assertTrue(os.path.exists('test_color.png'))
