import numpy as np
from PIL import Image
import json
import time

class Painter:
    def __init__(self):
        self.colours = json.loads(open(r"colours.json", "r", encoding="UTF-8").read())
    def clear(self, w, h):
        self.pixels = []
        for y in range(h):
            self.pixels.append([])
            for x in range(w):
                self.pixels[-1].append(tuple([255, 255, 255]))
        return self.pixels
    def convert(self, c):
        return tuple(self.colours[c])
    def set(self, x, y, c):
        self.pixels[y][x] = c
    def saveImage(self):
        self.array = np.array(self.pixels, dtype=np.uint8)
        self.image = Image.fromarray(self.array)
        self.image.save(f'out/new.png')