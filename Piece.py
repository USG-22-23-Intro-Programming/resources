# Piece Class
from graphics import *

class Piece:

    def __init__(self, pos, name, win):

        point = Point(pos[0]*80 + 140, pos[1]*80+140)
        self.image = Circle(point, 30)
        self.image.draw(win)
        self.name = name
        self.T = Text(point, name)
        self.T.draw(win)
        self.x = pos[0]
        self.y = pos[1]

    def getName(self):
        return self.name

    def getPos(self):
        return [self.x, self.y]

    def pawnMove(self):
        possibleMoves = []
        newY = self.y - 1
        possibleMoves.append([self.x, newY])
        return possibleMoves

    def knightMove(self):
        possibleMoves = []
        directions = [[1,1], [1, -1], [-1, 1], [-1, -1]]
        for d in directions:
            x = self.x + d[0]
            y = self.y + d[1]*2
            possibleMoves.append([x, y])
            x = self.x + d[0]*2
            y = self.y + d[1]
            possibleMoves.append([x, y])

        return possibleMoves

    def rookMove(self):
        possibleMoves = []
        for i in range(8):
            if i != self.x:
                possibleMoves.append([self.x, i])
            if i != self.y:
                possibleMoves.append([i, self.y])
        return possibleMoves

    def bishopMove(self):
        possibleMoves = []
        directions = [[1,1], [1, -1], [-1, 1], [-1, -1]]
        for d in directions:
            for i in range(1, 8):
                x = self.x + d[0]*i
                y = self.y + d[1]*i
                if (x > 7) or (y > 7) or (x < 0) or (y < 0):
                      break
                possibleMoves.append([x, y])
        return possibleMoves

    def kingMove(self):
        possibleMoves = []
        above = self.y - 1
        below = self.y + 1
        right = self.x + 1
        left = self.x - 1
        
        possibleMoves = [[left,above], [left,below], [right,above],
                             [right,below], [right, self.y], [left, self.y],
                             [self.x, above], [self.x, below]]
        return possibleMoves

    def move(self):    

        if self.name == "pawn":
            return self.pawnMove()

        if self.name == "queen":
            return self.bishopMove() + self.rookMove()

        if self.name == "king":
            return self.kingMove()

        if self.name == "rook":
            return self.rookMove()
            
        if self.name == "bishop":
            return self.bishopMove()

        if self.name == "knight":

            return self.knightMove()






