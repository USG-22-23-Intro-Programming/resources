from graphics import*
from Button import*

def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red - 50
            green = green - 50
            blue = blue - 50

            #print([red, green, blue])
            c = color_rgb(abs(red), abs(green), abs(blue))
            img.setPixel(i, j, c)


def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("cyan")

    I = Image(Point(300, 300), "cats.png")
    I.draw(win)

    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Darken")
    B2 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Lighten")

    Q = Button(win, Point(600, 300), Point(700, 375), "misty rose", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            

        #if B2.isClicked(m):
            

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
