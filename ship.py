import pyxel
class ship:
    def __init__(self):
       self.color=1 
       self.pos=100

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.move(-1)
        elif pyxel.btn(pyxel.KEY_D):
            self.move(1)


    def draw(self):
        pyxel.rect(self.pos+4,202,self.pos+6,199,self.color)
        pyxel.rect(self.pos,202,self.pos+10,205,self.color)

    def move(self,direction):
        if direction is -1:
            print("left")
            self.pos -= 1
        if direction is 1:
            print("right")
            self.pos += 1
        
