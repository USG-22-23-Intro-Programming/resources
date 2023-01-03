# Piece Class
from graphics import *

class Piece:

    def __init__(self, board, pos, name, color, win):

        self.point = Point(pos[0]*80 + 140, pos[1]*80+140)
        self.board = board
        self.image = Circle(self.point, 30)
        self.image.draw(win)
        self.image.setFill(color)
        self.name = name
        self.color = color
        self.T = Text(self.point, name)
        self.T.draw(win)
        self.T.setTextColor("cyan")
        self.x = pos[0]
        self.y = pos[1]

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getPos(self):
        return [self.x, self.y]

    def movePos(self, newPos):
        point2 = Point(newPos[0]*80 + 140, newPos[1]*80+140)
        diffX = point2.getX() - self.point.getX()
        diffY = point2.getY() - self.point.getY()
        self.image.move(diffX, diffY)
        self.T.move(diffX, diffY)
        self.point = point2
        self.x = newPos[0]
        self.y = newPos[1]

    def pawnMove(self, takenPos):
        possibleMoves = []
        addMoves = []
        if self.color == "white":
            d = -1
        else:
            d = 1
        newY = self.y + d
        if not ([self.x, newY] in takenPos):
            addMoves.append([self.x, newY])
        attacks = [[self.x - 1, newY], [self.x + 1, newY]]
        for a in attacks:
            if a in takenPos:
                if self.color != self.board.getSquare(a).getPiece().getColor():
                    addMoves.append(a)
        for move in addMoves:
            if (-1 < move[0] < 8) and (-1 < move[1] < 8):
                possibleMoves.append(move)
        return possibleMoves

    def knightMove(self, takenPos):
        possibleMoves = []
        directions = [[1,1], [1, -1], [-1, 1], [-1, -1]]
        for d in directions:
            x = self.x + d[0]
            y = self.y + d[1]*2
            if (-1 < x < 8) and (-1 < y < 8):
                if not ([x,y] in takenPos): 
                    possibleMoves.append([x, y])
                elif self.color != self.board.getSquare([x,y]).getPiece().getColor():
                    possibleMoves.append([x, y])
            x = self.x + d[0]*2
            y = self.y + d[1]
            if (-1 < x < 8) and (-1 < y < 8):
                if not ([x,y] in takenPos):
                    possibleMoves.append([x, y])
                elif self.color != self.board.getSquare([x,y]).getPiece().getColor():
                    possibleMoves.append([x, y])
            
        return possibleMoves

    def rookMove(self, takenPos):
        possibleMoves = []
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for d in directions:
            for i in range(1, 8):
                x = self.x + d[0]*i
                y = self.y + d[1]*i
                if (x > 7) or (y > 7) or (x < 0) or (y < 0):
                    break
                if [x,y] in takenPos:
                    if self.color != self.board.getSquare([x,y]).getPiece().getColor():
                        possibleMoves.append([x, y])
                    break
                possibleMoves.append([x, y])
        return possibleMoves

    def bishopMove(self, takenPos):
        possibleMoves = []
        directions = [[1,1], [1, -1], [-1, 1], [-1, -1]]
        for d in directions:
            for i in range(1, 8):
                x = self.x + d[0]*i
                y = self.y + d[1]*i
                if (x > 7) or (y > 7) or (x < 0) or (y < 0):
                    break
                if [x,y] in takenPos:
                    if self.color != self.board.getSquare([x,y]).getPiece().getColor():
                        possibleMoves.append([x, y])
                    break
                possibleMoves.append([x, y])
        return possibleMoves

    def kingMove(self):
        possibleMoves = []
        above = self.y - 1
        below = self.y + 1
        right = self.x + 1
        left = self.x - 1
        
        addMoves = [[left,above], [left,below], [right,above],
                             [right,below], [right, self.y], [left, self.y],
                             [self.x, above], [self.x, below]]
        for move in addMoves:
            if (-1 < move[0] < 8) and (-1 < move[1] < 8):
                possibleMoves.append(move)
        return possibleMoves

    def move(self, takenPos):    

        if self.name == "pawn":
            possibleMoves = self.pawnMove(takenPos)
            return possibleMoves

        if self.name == "queen":
            return self.bishopMove(takenPos) + self.rookMove(takenPos)

        if self.name == "king":
            possibleMoves = self.kingMove()
            for move in takenPos:
                if move in possibleMoves:
                    if self.color == self.board.getSquare(move).getPiece().getColor():
                        possibleMoves.remove(move)
            return possibleMoves

        if self.name == "rook":
            return self.rookMove(takenPos)
            
        if self.name == "bishop":
            return self.bishopMove(takenPos)

        if self.name == "knight":
            return self.knightMove(takenPos)







