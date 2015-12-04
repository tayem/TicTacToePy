player = 1;
win = 0;
fillCount  = 0;
class square:
    def __init__(self, sX, sY, sWidth, sHeight, filled, fillType):
        self.sWidth = sWidth;
        self.sHeight = sHeight;
        self.filled = filled;
        self.fillType = fillType;
        self.sX = sX;
        self.sY = sY;
    def FillX(self):
        global fillCount;
        self.filled = True;
        self.fillType = 1;
        fillCount += 1;
    def FillY(self):
        global fillCount;
        self.filled = True;
        self.fillType = 2;
        fillCount += 1;
    def Draw(self):
        if fillType == 0:
            rect(self.sX, self.sY, self.sWidth, self.sHeight);
         
def setup():
    size(900, 900);
    smooth();
    squareList = [];
    xLoc = 0;
    yLoc = 0;
    drawCount = 0;
    for i in range(9):
        currSquare = square(xLoc,yLoc,300,300,False,0);
        squareList.append(currSquare);
        xLoc += 300;
        squareList[i].Draw();
        drawCount += 1;
        if drawCount == 3:
            yLoc = 300;
            xLoc = 0;
        if drawCount == 6:
            yLoc = 600;
            xLoc = 0;
def draw():
    return None