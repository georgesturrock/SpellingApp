int circleSize = 0;

void setup () {
size(1200, 700);
background(0);
}

void draw () {
  if (mousePressed) {
    fill(255, 0, 0);
    stroke(255, 0, 0);
    circleSize = 15;
    ellipse(mouseX, mouseY, circleSize, circleSize);
    //circleSize++;
    } 
    else 
    {
    circleSize = 0;
    }
}
