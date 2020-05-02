"""Docstring
"""

import matplotlib.pyplot as plt


class Image():
    def __init__(self, screen_width=1920, screen_height=1080, zoom=0):
        self.screen_width = screen_width
        self.screen_height = screen_height

        if zoom <= -0.5 or zoom >= 0.5:
            raise ValueError('zoom must be greater than -0.5 and less than 0.5')

        self.zoom = zoom

        self.fig = None

    @staticmethod
    def _calculate_color(i, length):
        proportion = i / length
        color_value = round(proportion * (256 * 2))  # number of possible colors

        divisions = color_value // 256
        remainder = color_value % 256
        color = (0.0, 0.0, 0.0)

        if divisions == 0:
            color = ((255 - remainder) / 256, remainder / 256, 0)
        elif divisions == 1:
            color = (0, (255 - remainder) / 256, remainder / 256)

        return color

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
            for i, p in enumerate(points[1:]):
                color = self._calculate_color(i, len(points))
                ax.plot((points[i][0], p[0]), (points[i][1], p[1]), color=color)
        else:
            ax.plot(*zip(*points), color="black")

    def write(self, filename):
        self.fig.savefig(filename)

    def close(self):
        plt.close(self.fig)
