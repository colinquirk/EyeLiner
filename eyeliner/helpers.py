"""Docstring
"""
import os

import dask.dataframe as dd

import eyeliner.image


def make_image(d, group_columns, x_col, y_col, chunk, keep_last_chunk, base_path, color, **kwargs):
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
            img = eyeliner.image.Image(**kwargs)
            img.draw(chunk_points, color=color)
            img.write(os.path.join(base_path, fname))
            img.close()
            del img
    else:
        fname = '_'.join(group_values) + '.png'
        img = eyeliner.image.Image(**kwargs)
        img.draw(points, color=color)
        img.write(os.path.join(base_path, fname))
        img.close()
        del img


def make_images_from_df(df, group_columns, x_col='x', y_col='y', color=False, chunk=None,
                        keep_last_chunk=True, base_path='.', num_workers=1, **kwargs):

    df.groupby(group_columns).apply(
        make_image, group_columns=group_columns, x_col=x_col, y_col=y_col, color=color,
        chunk=chunk, keep_last_chunk=keep_last_chunk, base_path=base_path,
        meta={x_col: 'f8', y_col: 'f8'}, **kwargs).compute(num_workers=num_workers)
