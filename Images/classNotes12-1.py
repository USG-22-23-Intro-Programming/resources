from graphics import*
from Button import*


def fixGrayscale(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if ((red == green) and (red == blue)):
                c = color_rgb(255, 255, 255)
                img.setPixel(i, j, c)

            
    

def main():

    win = GraphWin("Image Example", 800, 600)
    win.setBackground('white')

    P = Image(Point(400, 300), "pulisic.png")
    P.draw(win)

    

    B = Image(Point(200, 500), "soccerball.png")
    B.draw(win)

    m = win.getMouse()

    message = fixGrayscale(P)
    print(message)

    B.move(-150, -100)


if __name__ == "__main__":
    main()
