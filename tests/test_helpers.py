import glob
import os
import unittest

import pandas as pd

import eyeliner


class TestHelpers(unittest.TestCase):

    def tearDown(self):
        for f in glob.glob('*.png'):
            os.remove(f)

    def test_make_image(self):
        fname = '1_1.png'

        df = pd.read_csv('tests/data/test.csv')

        eyeliner.make_image(df, ['subject', 'trial'], 'x', 'y', chunk=None, keep_last_chunk=False,
                            base_path='.')

        self.assertTrue(os.path.exists(fname))

    def test_make_images_from_df(self):
        df = pd.read_csv('tests/data/test.csv')

        eyeliner.make_images_from_df(df, ['subject', 'trial'])

        for i in range(1, 5):
            self.assertTrue(os.path.exists(f'1_{i}.png'))

    def test_make_images_from_df_with_args(self):
        df = pd.read_csv('tests/data/test.csv')

        eyeliner.make_images_from_df(df, ['subject', 'trial'], x_col='x', y_col='y', base_path='.')

        for i in range(1, 5):
            self.assertTrue(os.path.exists(f'1_{i}.png'))

    def test_make_images_from_df_with_chunks(self):
        df = pd.read_csv('tests/data/test.csv')

        eyeliner.make_images_from_df(df, ['subject', 'trial'], x_col='x', y_col='y', base_path='.',
                                     chunk=2000)

        for i in range(1, 4):
            for j in range(2):
                self.assertTrue(os.path.exists(f'1_{i}_{j}.png'))

    def test_make_images_from_df_no_last_chunk(self):
        df = pd.read_csv('tests/data/test.csv')

        eyeliner.make_images_from_df(df, ['subject', 'trial'], x_col='x', y_col='y', base_path='.',
                                     chunk=1000, keep_last_chunk=False)

        for i in range(1, 4):
            for j in range(5):
                self.assertTrue(os.path.exists(f'1_{i}_{j}.png'))
