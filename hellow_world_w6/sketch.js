var ballX = 500;
var ballY = 0;

var ballXV = -8;
var ballYV = 5;

var rectX;
var rectY;
var rect2X;
var rect2Y;

var score1 = 0;
var score2 = 0;

var r;
var g;
var b;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
  noStroke();
  fill(0, 255, 0);   

  rectX = 10;
  rectY = windowHeight/2;
  rect2X = windowWidth-50;
  rect2Y = windowHeight/2;
}


function draw() {
  background(30);  
  setText();
  setShapes();    
  bounceCheck();
  increment();
  // scoreCheck();  
  sliderConstrain();
  keyTyped()
}

function sliderConstrain(){
  if (rectY < 0){
    rectY = 0;
  }else if(rectY + 120 > windowHeight){
    rectY = windowHeight - 120;
  }

  if (rect2Y < 0){
    rect2Y = 0;
  }else if(rect2Y + 120 > windowHeight){
    rect2Y = windowHeight - 120;
  }
}

function increment() {  
  ballX += ballXV;  
  ballY += ballYV;
  
  // if(millis() % 1000 == 0) {
  //   ballXV = ballXV * 2;
  // }
}

// function mouseMoved() {
//   rectY = mouseY;
// }

function keyTyped() {
  if (key === 's' && keyIsPressed ) {
    rectY += 10;
  } else if (key === 'w' && keyIsPressed) {
    rectY -= 10;
  }

  if (key === 'l' && keyIsPressed ) {
    rect2Y += 10;
  } else if (key === 'o' && keyIsPressed) {
    rect2Y -= 10;
  }
}

function ball(x, y) {
  ellipse(x, y, 30, 30);
}

function setShapes() {
  fill(255);
  rect(rectX, rectY, 20, 120);
  rect(rect2X, rect2Y, 20, 120);
  fill(r, g, b);
  ball(ballX, ballY);
}

function sliderBounce1() {
  if(rectY < ballY && rectY + 120 > ballY) {
    ballXV = ballXV * -1;
    score1 += 1;
    changeColor();
  }
}

function sliderBounce2() {
  if(rect2Y < ballY && rect2Y + 120 > ballY) {
    ballXV = ballXV * -1;
    score2 += 1;
    changeColor();
  }
}

function changeColor(){
  r = 255;
  g = random(100); // g is a random number betwen 100 - 200
  b = random(255); // b is a random number between 0 - 100
}

function wallBounce() {
  ballXV = ballXV * -1;
}

function bounceCheck() {
  if(ballY < 0 || ballY + 15 > windowHeight) {
    ballYV = ballYV * -1;
  }
  
  if(ballX < 40 && ballXV < 0) {
    sliderBounce1();
  }
  
  if(ballX > windowWidth - 60 && ballXV > 0) {
    sliderBounce2();
  }
  
  if(ballX + 15 > windowWidth && ballXV > 0) {
    wallBounce();
  }

  if(ballX - 15 < 0 && ballXV < 0) {
    wallBounce();
  }
  
  if(ballX  < 0) {
    ballX = ballXV * -1;
  }
}

// function scoreCheck() {
//   if(score == 0) {
//     noLoop();
//     score = "YOU LOSE";
//   }
  
//   if(score == 10) {
//     noLoop();
//     score = "YOU WIN";
//   }
// }

function setText() {
  fill(255);
  textAlign(CENTER);
  textSize(22);
  text("player 1: " + score1, 80, 40);
  text("player 2: " + score2, windowWidth-100, 40);
}