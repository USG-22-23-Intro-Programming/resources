# Chessboard Class and Main method

from graphics import *
from Square import *
from Button import *

class Chessboard:

    def __init__(self, win):

        self.win = win
        self.board = [[],[],[],[],[],[],[],[]]
        for i in range(8):
            for j in range(8):
                self.board[i].append(Square(Point(100 + 80*i, 100 + 80*j), win))

        self.takenPos = []
        for i in range(8):
            self.takenPos.append([i,0])
            self.takenPos.append([i,1])
            self.takenPos.append([i,6])
            self.takenPos.append([i,7])
        self.highlighted = []
        self.currentSquare = None

    def curS(self, s):
        self.currentSquare = s

    def getTaken(self):
        return self.takenPos
            
    def addHighlight(self, square):
        square.highlight()
        self.highlighted.append(square)

    def getHighlights(self):
        return self.highlighted

    def removeHighlights(self):
        for s in self.highlighted:
            s.unHighlight()

    def getClick(self, m):
        for i in range(8):
            for j in range(8):
                if self.board[i][j].isClicked(m):
                    return self.board[i][j]
        return False

    def getSquare(self, pos):
        return self.board[pos[0]][pos[1]]

    def move(self, pos):
        newS = self.board[pos[0]][pos[1]]
        p = self.currentSquare.getPiece()
        p.movePos(pos)
        newS.addPiece(p)
        if not (pos in self.takenPos):
            self.takenPos.append(pos)
        self.takenPos.remove(self.currentSquare.getPos())
        self.currentSquare.removePiece()
        
    

def main():

    win = GraphWin("Chess example", 1000, 800)

    Q = Button(win, Point(750, 680), Point(850, 760), "tomato", "QUIT")

    C = Chessboard(win)

    bPieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
    for i in range(8):
        C.getSquare([i,0]).addPiece(Piece(C, [i,0], bPieces[i], "black", win))
        C.getSquare([i,1]).addPiece(Piece(C, [i,1], "pawn", "black", win))
        C.getSquare([i,7]).addPiece(Piece(C, [i,7], bPieces[i], "white", win))
        C.getSquare([i,6]).addPiece(Piece(C, [i,6], "pawn", "white", win))

    while True:
        m = win.getMouse()

        if Q.isClicked(m):
            break

        B = C.getClick(m)
        if B:
            if B in C.getHighlights():
                C.move(B.getPos())
                C.removeHighlights()

            else:
                C.removeHighlights()
                if B.hasPiece():
                    C.curS(B)
                    name = B.getPiece().getName()
                    pos = B.getPiece().getPos()
                    possibleMoves = B.getPiece().move(C.getTaken())
                    #print("The " + name + " at " + str(pos) + " can move:")
                    #print(possibleMoves)
                    for p in possibleMoves:
                        C.addHighlight(C.getSquare(p))

    win.close()

    

if __name__ == "__main__":
    main()
