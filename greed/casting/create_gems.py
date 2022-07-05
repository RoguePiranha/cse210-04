import random

from casting.artifact import Artifact
from casting.cast import Cast

from shared.color import Color
from shared.point import Point

COLS = 60
CELL_SIZE = 15
FONT_SIZE = 15

class new_gems:
    def create_gems(self, quantity):
        cast = Cast()

        for n in range(quantity):
            text = chr(random.choice([42, 111]))

            # start positions for the artifacts
            x = random.randint(1, COLS - 1)
            y = 0
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_value()
            artifact.set_velocity(Point(0, 3))
            artifact.set_position(position)
            cast.add_actor("artifacts", artifact)