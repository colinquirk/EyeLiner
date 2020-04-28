"""Docstring
"""
import os

import eyeliner.image


def make_image(d, group_columns, x_col, y_col, chunk, keep_last_chunk, base_path):
    group_values = [str(int(i)) for i in list(d[group_columns].iloc[0])]
    points = list(zip(d[x_col], d[y_col]))

    if chunk is not None and len(points) > chunk:
        for i in range(len(points) // chunk):
            fname = '_'.join(group_values + [str(i)]) + '.png'
            chunk_start = chunk * (i)
            chunk_end = chunk * (i + 1)

            if not keep_last_chunk and chunk_end > len(points):
                continue

            chunk_points = points[chunk_start:chunk_end]
            img = eyeliner.image.Image()
            img.draw(chunk_points, color=True)
            img.write(os.path.join(base_path, fname))
    else:
        fname = '_'.join(group_values) + '.png'
        img = eyeliner.image.Image()
        img.draw(points, color=True)
        img.write(os.path.join(base_path, fname))


def make_images_from_df(df, group_columns, x_col='x', y_col='y', chunk=None, keep_last_chunk=True,
                        base_path=None):
    groups = df.groupby(group_columns)
    groups.apply(make_image, group_columns=group_columns, x_col=x_col, y_col=y_col,
                 chunk=chunk, keep_last_chunk=keep_last_chunk, base_path=base_path)
