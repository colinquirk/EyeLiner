"""Docstring
"""

import matplotlib.pyplot as plt


class Image():
    def __init__(self, screen_width=1920, screen_height=1080, zoom=0):
        if zoom <= -0.5 or zoom >= 0.5:
            raise ValueError('zoom must be greater than -0.5 and less than 0.5')

        self.zoom = zoom
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.colors = [
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 1],
            [0, 0, 1]
        ]

        self.fig = None

    @staticmethod
    def get_chunks(points):
        points_per_chunk = len(points) // 5

        point_chunks = []
        for i in range(5):
            if i == 4:
                point_chunks.append(points[i * points_per_chunk:])
            else:
                point_chunks.append(points[i * points_per_chunk:i * points_per_chunk + points_per_chunk])

        return point_chunks

    def draw(self, points, color=False):
        try:
            points[0][1]
        except (TypeError, KeyError, IndexError):
            raise(TypeError('Points should be a list of length 2 (x,y) tuples.'))

        if len(points[0]) != 2:
            raise(TypeError('Length of each point (x,y) must be equal to 2.'))

        x_zoom_offset = self.zoom * self.screen_width
        y_zoom_offset = self.zoom * self.screen_height

        self.fig, ax = plt.subplots(figsize=(4, 4), dpi=56)
        ax.axis('off')
        ax.set_xlim(x_zoom_offset, self.screen_width - x_zoom_offset)
        ax.set_ylim(y_zoom_offset, self.screen_height - y_zoom_offset)

        if color:
            point_chunks = self.get_chunks(points)
            for i, p in enumerate(point_chunks):
                ax.plot(*zip(*p), color=self.colors[i])
        else:
            ax.plot(*zip(*points), color="black")

    def write(self, filename):
        self.fig.savefig(filename)

    def close(self):
        self.fig.clear()
        plt.close(self.fig)
