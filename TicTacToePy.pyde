player = 1;
win = 0;
class square:
    fillCount = 0;
    def __init__(self, sWidth, sHeight, filled, fillType):
        self.sWidth = sWidth;
        self.sHeight = sHeight;
        self.filled = filled;
        self.fillType = fillType;
    def fillX(self):
        self.filled = True;
        self.fillType = 1;
        fillCount += 1;
    def fillY(self):
        self.filled = True;
        self.fillType = 2;
        fillCount += 1;
        
def setup():
    fullScreen();
    smooth();
    
def draw():
    return None