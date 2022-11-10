from graphics import*
from Button import*


def main():

    win = GraphWin("character creator", 800, 600)
    win.setBackground("cyan")

    C = Circle(Point(300, 300), 150)
    C.draw(win)

    #R = Rectangle(Point(200, 500), Point(400, 575))
    #R.draw(win)

    #L = Line(Point(0, 0), Point(800, 600))
    #L.draw(win)

    BigEye1 = Circle(Point(200, 250), 50)
    BigEye2 = Circle(Point(400, 250), 50)

    smallEye1 = Circle(Point(250, 250), 20)
    smallEye2 = Circle(Point(350, 250), 20)

    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Big Eyes")
    B2 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Small Eyes")

    Q = Button(win, Point(600, 300), Point(700, 375), "misty rose", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            BigEye1.undraw()
            BigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()
            
            BigEye1.draw(win)
            BigEye2.draw(win)

        if B2.isClicked(m):
            smallEye1.undraw()
            smallEye2.undraw()
            BigEye1.undraw()
            BigEye2.undraw()
            
            smallEye1.draw(win)
            smallEye2.draw(win)

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
