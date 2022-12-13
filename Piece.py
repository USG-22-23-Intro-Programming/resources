# Piece Class
from graphics import *

class Piece:

    def __init__(self, pos, name, win):

        self.image = Circle(pos, 30)
        self.image.draw(win)
        self.name = name
        self.T = Text(pos, name)
        self.T.draw(win)
        self.x = ((pos.getX() - 140)//80)
        self.y = ((pos.getY() - 140)//80)

    def getName(self):
        return self.name

    def getPos(self):
        return [self.x, self.y]

    def move(self):
        possibleMoves = []
        if self.name == "knight":
            possibleMoves.append([3,6])
            #move like a knight
        return False
