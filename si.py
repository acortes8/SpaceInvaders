import pyxel
import ship
import invaders

class si:
    def __init__(self):
        self.p=ship.ship()
        self.i=[]
        self.i.append(invaders.invaders(11,30,30))

    def draw(self):
        self.p.draw()
        for inv in self.i:
            inv.draw()

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
            for invader in self.i:
                if invader.x < bullet.pos+5 and invader.x+4 > bullet.pos+6 and invader.y > bullet.y:
                    self.p.bullets.remove(bullet)
                    self.i.remove(invader)
             
        #for inv in self.i:
        #    inv.update()
        


