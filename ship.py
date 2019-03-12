import pyxel
class ship:
    def __init__(self):
        self.color=1 
        self.pos=100
        self.bullets=[] 

    #def update(self):
        


    def draw(self):
        pyxel.rect(self.pos+4,202,self.pos+6,199,self.color)
        pyxel.rect(self.pos,202,self.pos+10,205,self.color)
        for bullet in self.bullets:
            bullet.draw()


    def move(self,direction):
        if direction is -1 and self.pos is not 0:
            print("left")
            self.pos -= 1
        if direction is 1 and self.pos is not 189:
            print("right")
            self.pos += 1
        
    def shoot(self):
        print("bang")
        self.bullets.append(projectile(self.pos))




class projectile:
    def __init__(self,pos):
        self.pos=pos
        self.y=199

    def update(self):
        self.y-=2
        
    def draw(self):
        pyxel.rect(self.pos+5,self.y,self.pos+6,self.y+4,9)


