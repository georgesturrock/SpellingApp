# Libraries
add_library("sound")

# Global variables
## sh words
###wordList = ['ship', 'shark', 'fish', 'push', 'rash']
## ch words
wordList = ['chap', 'ranch', 'lunch', 'inch', 'nacho']
wordPointer = 0
w = 1200
h = 700
endL = len(wordList[wordPointer])
count = 0

def setup():
    size(w, h)
    background(0)
    frameRate(90)
    #global sf
    #sf = SoundFile(this, wordList[0]+".wav")

def draw():
    controls()
    wordBoxes(wordList[wordPointer])
    soundIcon()
    if (mousePressed):
        fill(255, 0, 0)
        stroke(255, 0, 0)
        circleSize = 15
        ellipse(mouseX, mouseY, circleSize, circleSize)
    else:
        circleSize = 0
        
def wordBoxes(letters):
    textSize(90)
    fill(255,255,255)
    text(wordList[wordPointer][0:endL], (w/2 - 80), 250)
    boxWidth = w/len(letters)
    i = 0
    for l in letters:
        noFill()
        stroke(255,255,255)
        rect((i*boxWidth), 400, boxWidth, 300)
        i = i + 1
    
def controls():
    cw = w/3
    l = len(wordList[wordPointer])
    #control boxes
    strokeWeight(4)
    ### start over box
    if  (mousePressed) and (mouseX < cw) and (mouseY < 100):
        stroke(255,0,0)
        background(0)
        global wordPointer
        wordPointer = 0
        global endL 
        endL = len(wordList[wordPointer])
        global count
        count = 0
    else:
        stroke(0)
    fill(0xFF028A0F)
    rect(0, 0, cw, 100)
    ### next box
    if  (mousePressed) and (mouseX > cw) and (mouseX < cw*2) and (mouseY < 100):
        stroke(255,0,0)
        delay(1000)
        global count
        count = count + 1
        global endL
        endL = l - count
        if (endL < 0):
            global wordPointer
            wordPointer = wordPointer +1
            if (wordPointer == len(wordList)):
                global wordPointer
                wordPointer = 0
            global endL
            endL = len(wordList[wordPointer])
            global count
            count = 0
        background(0)
       # print('word', wordList[wordPointer])
       # print('count', count)
       # print('endL', endL)
       # print('wordPointer', wordPointer)
    else:
        stroke(0)
    fill(0xFF000080)
    rect(cw*1, 0, cw, 100)
    ### erase box
    if  (mousePressed) and (mouseX > cw*2) and (mouseX < w) and (mouseY < 100):
        stroke(255,0,0)
        background(0)
    else:
        stroke(0)
    fill(0xFFFFD300)
    rect(cw*2, 0, cw, 100)
    #control box text
    fill(255)
    textSize(38)
    text('Start Over', cw/3.5, 60) #95
    text('Next', cw*1.3, 60) #550
    text('Erase', cw*2.3, 60) #950
    
def soundIcon():
    sx = w/9
    sy = h/3
    stroke(255)
    strokeWeight(4)
    fill(0)
    rect(sx-15, sy*.8, sx*0.7, sy*.4) 
    noFill()
    #arc(x, y, width, height, radians-start angle, radiand-end angle)
    arc(sx, sy, 80, 80, radians(340), radians(360))
    arc(sx, sy, 80, 80, radians(0), radians(20))
    arc(sx, sy, 100, 100, radians(340), radians(360))
    arc(sx, sy, 100, 100, radians(0), radians(20))
    arc(sx, sy, 120, 120, radians(340), radians(360))
    arc(sx, sy, 120, 120, radians(0), radians(20))
    fill(255)
    triangle(sx+5, sy, sx+20, sy-8, sx+20, sy+8)
    if (mousePressed):
        if (mouseX > sx-15) and (mouseX < ((sx-15)+(sx*.7))) and (mouseY > sy*0.8) and (mouseY < ((sy*.8)+(sy*0.4))):
            playSound()
#        else:
#            print("mouseX", mouseX)
#            print("mouseY", mouseY)
#            print("left X", sx-15)
#            print("right X", (sx-15)+(sx*.7))
#            print("top Y", sy*.8)
#            print("bottom Y", (sy*.8)+(sy*0.4))
    
def playSound():
    print("Turn up the volume")
    #sf.play()
    delay(500)
