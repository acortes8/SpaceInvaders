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
        if pyxel.btn(pyxel.KEY_A):
            self.p.move(-1)
        elif pyxel.btn(pyxel.KEY_D):
            self.p.move(1)
            
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.p.shoot()

        for bullet in self.p.bullets:
            bullet.update()
            if bullet.y<-5:
                self.p.bullets.remove(bullet)

        self.i.update()
        


