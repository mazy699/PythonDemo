from tkinter import *
from math import sin, cos, pi
import random

CANVAS_WIDTH = 648
CANVAS_HEIGHT = 480
CANVAS_CENTER_X = CANVAS_WIDTH / 2
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
IMAGE_ENLARGE = 8


def heart_funcion(t):
    # base function
    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))

    # enlarge
    x *= IMAGE_ENLARGE
    y *= IMAGE_ENLARGE

    # shift
    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y

    # return the coordinates of the heart
    return int(x), int(y)


def scatter_inside(x, y, beta=0.15):
    ratiox = - beta * log(random.random())
    ratioy = - beta * log(random.random())
    dx = ratiox * (x-CANVAS_CENTER_X)
    dy = ratioy * (y-CANVAS_CENTER_Y)
    return x-dx, y-dy


def shrink(x, y, ratio):
    force = 1/(((x-CANVAS_CENTER_X)**2+(y-CANVAS_CENTER_Y)**2)**0.5)
    dx = ratio*force*(x-CANVAS_CENTER_X)
    dy = ratio*force*(y-CANVAS_CENTER_Y)
    return x-dx, y-dy


class Heart:
    def __init__(self):
        self.points = set()
        self.build(2000)

    def build(self, number):
        # Heart
        for _ in range(number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_funcion(t)
            self.points.add((int(x), int(y)))

# Heart immediate inside
        for xx, yy in list(self.points):
            for _ in range(3):
                x, y = scatter_inside(xx, yy, 0.05)
                self._extra_points.add((x, y))

        # Inside
        points_list = list(self.points)
        for _ in range(4000):
            x, y = random.choice(points_list)
            x, y = scatter_inside(x, y)
            self._inside.add((int(x), int(y)))

    def calc_position(self, x, y, ratio):
        force = 1 / (((x - CANVAS_CENTER_X) ** 2 +
                     (y - CANVAS_CENTER_Y) ** 2) ** 0.5)
        dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)
        return x-dx, y-dy

    def calc(self, frame):
        calc_position = self.calc_position
        ratio = 10 * sin(frame / 10 * pi)
        all_points = []

        # outline
        for x, y in self.points:
            x, y = calc_position(x, y, ratio)
            size = random.randint(1, 3)
            all_points.append((x, y, size))

        # inner
        for x, y in self._extra_point:
            x, y = calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        # inside
        for x, y in self._inside:
            x, y = calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        self.all_points[frame] = all_points

    def render(self, canvas):
        for x, y in self.points:
            canvas.create_rectangle(x, y, x+1, y+1, width=0, fill='#ff7171')


def draw(root: Tk, canvas: Canvas, heart: Heart, frame: 0):
    canvas.delete('all')
    heart.render(canvas)
    root.after(30, draw, root, canvas, heart, frame+1)


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, bg='black', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    points_list = []
    root.mainloop()
