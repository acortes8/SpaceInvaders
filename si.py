import pyxel
import ship
import invaders

class si:
    def __init__(self):
        self.p=ship.ship()
        self.i=invaders.invaders(11,30,30)

    def draw(self):
        self.p.draw()
        self.i.draw()

    def update(self):
        self.p.update()
        self.i.update()


