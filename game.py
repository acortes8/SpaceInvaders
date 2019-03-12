#!/usr/bin/python3
import si
import pyxel

class S_Invaders:
    def __init__(self):
        pyxel.init(200,250,caption="Space Invaders" ,fps=60)
        self.game=si.si()
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.game.update()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.game.draw() 


S_Invaders()

