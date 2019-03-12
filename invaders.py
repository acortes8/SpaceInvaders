import pyxel

class invaders:
    def __init__(self,color,x,y):
        self.color=color
        self.x=x
        self.y=y

    def update(self):
        print("'")
        
    def draw(self):
        pyxel.rect(self.x,self.y,self.x+4,self.y+4,self.color)        
