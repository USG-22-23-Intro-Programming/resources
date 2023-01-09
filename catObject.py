from graphics import *

class CatObject:

    def __init__(self, pos, win):
        self.x = pos[0]
        self.y = pos[1]
        self.win = win
        self.I = Image(Point(115 + self.x*30, 115 + self.y*30), "Cats.png")
        self.I.draw(win)

    def move(self):

        #move right 1 space
        self.x = self.x + 1
        deltaX = 1
        deltaY = 0
        self.I.move(30*deltaX, 30*deltaY)
        
        
