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