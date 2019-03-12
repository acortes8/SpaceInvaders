#!/usr/bin/python3
import ship
import pyxel

class S_Invaders:
    def __init__(self):
        pyxel.init(200,250,caption="Space Invaders" ,fps=60)
        self.p1=ship.ship()
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.p1.update()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.p1.draw() 


S_Invaders()

