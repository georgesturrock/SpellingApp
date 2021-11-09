# Global variables
wordList = ['said', 'dead', 'head', 'bread']
wordPointer = 0
w = 1200
h = 700
endL = len(wordList[wordPointer])
count = 0

def setup():
    size(w, h)
    background(0)
    frameRate(80)

def draw():
    controls()
    wordBoxes(wordList[wordPointer])
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
        print('word', wordList[wordPointer])
        print('count', count)
        print('endL', endL)
        print('wordPointer', wordPointer)
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
    text('Start Over', 95, 60)
    text('Next', 550, 60)
    text('Erase', 950, 60)
