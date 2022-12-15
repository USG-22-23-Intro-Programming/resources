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

    def getClick(self, m):
        for i in range(8):
            for j in range(8):
                if self.board[i][j].isClicked(m):
                    return self.board[i][j]
        return False

    def getSquare(self, x, y):
        return self.board[x][y]

def main():

    win = GraphWin("Chess example", 1000, 800)

    Q = Button(win, Point(750, 680), Point(850, 760), "tomato", "QUIT")

    C = Chessboard(win)
   
    k2 = Piece([2,4], "knight", win)
    p1 = Piece([3,5], "pawn", win)
    King = Piece([5,5], "king", win)
    r1 = Piece([0,0], "rook", win)
    b1 = Piece([1,4], "bishop", win)
    q1 = Piece([4,1], "queen", win)

    C.getSquare(4, 1).addPiece(q1)    
    C.getSquare(1, 4).addPiece(b1)
    C.getSquare(0,0).addPiece(r1)
    C.getSquare(2,4).addPiece(k2)
    C.getSquare(3,5).addPiece(p1)
    C.getSquare(5,5).addPiece(King)

    while True:
        m = win.getMouse()

        if Q.isClicked(m):
            break

        B = C.getClick(m)
        if B:
            if B.hasPiece():
                name = B.getPiece().getName()
                pos = B.getPiece().getPos()
                possibleMoves = B.getPiece().move()
                print("The " + name + " at " + str(pos) + " can move:")
                print(possibleMoves)

    win.close()

    

if __name__ == "__main__":
    main()
