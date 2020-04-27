"""Docstring
"""

import cairo


class Image():
    def __init__(self, out_size=224, screen_width=1920, screen_height=1080):
        self.out_size = out_size
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, screen_width, screen_height)
        self.context = cairo.Context(self.surface)

        self._setup_context()

    def _setup_context(self):
        self.context.scale(self.out_size / self.screen_width,
                           self.out_size / self.screen_height)

        # white background
        self.context.set_source_rgb(1., 1., 1.)
        self.context.rectangle(0, 0, self.screen_width, self.screen_height)
        self.context.fill()

    def draw(self, points, color=None):
        try:
            points[0][1]
        except (TypeError, KeyError, IndexError):
            raise(TypeError('Points should be a list of legnth 2 (x,y) tuples.'))

        if len(points[0]) != 2:
            raise(TypeError('Length of each point (x,y) must be equal to 2.'))

        self.context.move_to(points[0][0], points[0][1])

        for p in points:
            self.context.line_to(p[0], p[1])

        self.context.set_source_rgb(0., 0., 0.)
        self.context.set_line_width(10)
        self.context.stroke()

    def write(self, filename):
        self.surface.write_to_png(filename)
