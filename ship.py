import pyxel
class ship:
    def __init__(self):
       self.color=1 
       self.pos=100

    def update(self):
        print("f")

    def draw(self):
        pyxel.rect(self.pos+4,202,self.pos+6,199,self.color)
        pyxel.rect(self.pos,202,self.pos+10,205,self.color)
