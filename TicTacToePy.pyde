player = 1;
win = 0;
fillCount  = 0;
squareList = [];
class square:
    def __init__(self, sX, sY, sWidth, sHeight, filled, fillType):
        self.sX = sX;
        self.sY = sY;
        self.sWidth = sWidth;
        self.sHeight = sHeight;
        self.filled = filled;
        self.fillType = fillType;
    def Draw(self):
        if self.filled == False:
            if self.fillType == 0:
                fill(255);
                rect(self.sX, self.sY, self.sWidth, self.sHeight);
            elif self.fillType == 1:
                noFill();
                rect(self.sX, self.sY, self.sWidth, self.sHeight);
                stroke(3,55,255); 
                line(self.sX, self.sY, self.sX+self.sWidth, self.sY+self.sHeight);
                line(self.sX+self.sWidth, self.sY, self.sX, self.sY+self.sHeight);
                self.filled = True;
            elif self.fillType == 2:
                noFill();
                noStroke();
                rect(self.sX, self.sY, self.sWidth, self.sHeight);
                fill(255,31,31);
                ellipse(self.sX, self.sY, self.sWidth, self.sHeight);
                self.filled = True;
    def isClicked(self,mX, mY):
        if self.sX <= mX <= self.sX+self.sWidth and self.sY <= mY <= self.sY+self.sHeight:
            return True;
        else: return False;
        
def setup():
    size(900, 900);
    colorMode(RGB, 255,255,255);
    ellipseMode(CORNER);
    global squareList;
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
    return None;

def mouseClicked():
    global player;
    global fillCount;
    global squareList;
    i = 0;
    mloop = True;
    while i < 9 and mloop == True:
        if squareList[i].isClicked(mouseX, mouseY) == True and not squareList[i].filled:
            mloop = False;
            if player == 1:
                squareList[i].fillType = 1;
                fillCount += 1;
                player = 2;
            else:
                squareList[i].fillType = 2;
                fillCount+=1;
                player = 1;
            squareList[i].Draw();
        i+=1;
    if winDetection() == 1:
        rectMode(CENTER);
        fill(3,55,255);
        stroke(0,0,0);
        rect(450,450,800,800);
        fill(255,255,255);
        textSize(80);
        text("Player 1 Wins!", 200,450);
    elif winDetection() == 2:
        rectMode(CENTER);
        fill(255,31,31);
        stroke(0,0,0);
        rect(450,450,800,800);
        fill(255,255,255);
        textSize(80);
        text("Player 2 Wins!", 200,450);
def winDetection():
    global squareList;
    if squareList[0].fillType == squareList[1].fillType and squareList[0].fillType == squareList[2].fillType:
        if squareList[0].fillType == 1:
            return 1;
        elif squareList[0].fillType == 2:
            return 2;
    if squareList[3].fillType == squareList[4].fillType and squareList[3].fillType == squareList[5].fillType:
        if squareList[3].fillType == 1:
            return 1;
        elif squareList[3].fillType == 2:
            return 2;
    if squareList[6].fillType == squareList[7].fillType and squareList[6].fillType == squareList[8].fillType:
        if squareList[6].fillType == 1:
            return 1;
        elif squareList[6].fillType == 2:
            return 2;
    if squareList[0].fillType == squareList[3].fillType and squareList[0].fillType == squareList[6].fillType:
        if squareList[0].fillType == 1:
            return 1;
        elif squareList[0].fillType == 2:
            return 2;
    if squareList[1].fillType == squareList[4].fillType and squareList[1].fillType == squareList[7].fillType:
        if squareList[1].fillType == 1:
            return 1;
        elif squareList[1].fillType == 2:
            return 2;
    if squareList[2].fillType == squareList[5].fillType and squareList[2].fillType == squareList[8].fillType:
        if squareList[2].fillType == 1:
            return 1;
        elif squareList[2].fillType == 2:
            return 2;
    if squareList[0].fillType == squareList[1].fillType and squareList[0].fillType == squareList[2].fillType:
        if squareList[0].fillType == 1:
            return 1;
        elif squareList[0].fillType == 2:
            return 2;
    if squareList[0].fillType == squareList[4].fillType and squareList[0].fillType == squareList[8].fillType:
        if squareList[0].fillType == 1:
            return 1;
        elif squareList[0].fillType == 2:
            return 2;
    if squareList[2].fillType == squareList[4].fillType and squareList[2].fillType == squareList[6].fillType:
        if squareList[2].fillType == 1:
            return 1;
        elif squareList[2].fillType == 2:
            return 2;