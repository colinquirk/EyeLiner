"""Docstring
"""
import os

import eyeliner.image


def make_image(d, group_columns, x_col, y_col, base_path):
    group_values = [str(int(i)) for i in list(d[group_columns].iloc[0])]
    fname = '_'.join(group_values) + '.png'

    points = list(zip(d[x_col], d[y_col]))
    img = eyeliner.image.Image()
    img.draw(points, color=True)
    img.write(os.path.join(base_path, fname))


def make_images_from_df(df, group_columns, x_col='x', y_col='y', chunk=1000, base_path=None):
    groups = df.groupby(group_columns)
    groups.apply(make_image, group_columns=group_columns, x_col=x_col, y_col=y_col,
                 base_path=base_path)
