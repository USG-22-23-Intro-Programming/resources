from graphics import *
from Button import *
from catObject import *

def main():
    win = GraphWin("Shark Simulator", 800, 600)
 
    for i in range(14):
    
        p1 = Point(100 + i*30, 100)
        p2 = Point(100 + i*30, 500)
        l = Line(p1, p2)
        l.draw(win)

    for i in range(14):
        
        p1 = Point(100, 100 + i*30)
        p2 = Point(500, 100 + i*30)
        l = Line(p1, p2)
        l.draw(win)

    C = CatObject([1,1], win)
    B = Button(win, Point(450, 300), Point(550, 375), "red", "MOVE")

    while True:
        m = win.getMouse()

        if B.isClicked(m):
            C.move()




    

if __name__ == "__main__":
    main()
