"""Docstring
"""

import cairo


class Image():
    def __init__(self, out_size=224, screen_width=1920, screen_height=1080, zoom=1):
        self.out_size = out_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.zoom = zoom

        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, out_size, out_size)
        self.context = cairo.Context(self.surface)

        self._setup_context()

    def _setup_context(self):
        self.context.scale(self.out_size / self.screen_width,
                           self.out_size / self.screen_height)

        # white background
        self.context.set_source_rgb(1., 1., 1.)
        self.context.rectangle(0, 0, self.screen_width, self.screen_height)
        self.context.fill()

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

    def _zoom(self, points):
        center = (self.screen_width / 2, self.screen_height / 2)
        print(center)
        zeroed = [(x - center[0], y - center[1]) for x, y in points]
        print(zeroed[0])
        zoomed_zeroed = [(x * self.zoom, y * self.zoom) for x, y in zeroed]
        print(zoomed_zeroed[0])
        zoomed = [(x + center[0], y + center[1]) for x, y in zoomed_zeroed]
        print(zoomed[0])

        return zoomed

    def draw(self, points, color=False):
        try:
            points[0][1]
        except (TypeError, KeyError, IndexError):
            raise(TypeError('Points should be a list of length 2 (x,y) tuples.'))

        if len(points[0]) != 2:
            raise(TypeError('Length of each point (x,y) must be equal to 2.'))

        print('draw')
        print(points[0])
        points = self._zoom(points)
        print(points[0])
        print('done')

        self.context.set_line_width(10)
        self.context.move_to(points[0][0], points[0][1])
        self.context.set_source_rgb(0., 0., 0.)

        if color:
            for i, p in enumerate(points):
                self.context.set_source_rgb(*self._calculate_color(i, len(points)))
                self.context.move_to(points[i-1][0], points[i-1][1])
                self.context.line_to(p[0], p[1])
                self.context.stroke()
        else:
            for p in points:
                self.context.line_to(p[0], p[1])
            self.context.stroke()

    def write(self, filename):
        self.surface.write_to_png(filename)
