

var capture;
var w = 640;
var h = 480;
let ballX = 320;
let ballY = 180;
let xspeed = 10;
let yspeed = 4;

let r = 20;

function setup() {
    capture = createCapture({
        audio: false,
        video: {
            width: w,
            height: h
        }
    }, function() {
        console.log('capture ready.')
    });
    capture.elt.setAttribute('playsinline', '');
    capture.size(w, h);
    createCanvas(w, h);
    capture.hide();
}

var targetColor = [255, 255, 255];
function draw() {
    
  
    capture.loadPixels();
    var sampling = false;
    var sumPosition = createVector(0, 0);
    if (capture.pixels.length > 0) { // don't forget this!

        if (mouseIsPressed &&
            mouseX > 0 && mouseX < width &&
            mouseY > 0 && mouseY < height) {
            targetColor = capture.get(mouseX, mouseY);
            sampling = true;
        }

        var w = capture.width,
            h = capture.height;
        var i = 0;
        var pixels = capture.pixels;
        var thresholdAmount = select('#thresholdAmount').value();
        thresholdAmount /= 100.; // this is the slider range
        thresholdAmount *= 255 * 3; // this is the maximum value
        var total = 0;
        for (var y = 0; y < h; y++) {
            for (var x = 0; x < w; x++) {
                var diff =
                    Math.abs(pixels[i + 0] - targetColor[0]) +
                    Math.abs(pixels[i + 1] - targetColor[1]) +
                    Math.abs(pixels[i + 2] - targetColor[2]);
                var outputValue = 0;
                if (diff < thresholdAmount) {
                    outputValue = 0;
                    sumPosition.x += x;
                    sumPosition.y += y;
                    total++;
                }
                pixels[i++] = outputValue; // set red
                pixels[i++] = outputValue; // set green
                pixels[i++] = outputValue; // set blue
                i++; // skip alpha
            }
        }

        sumPosition.div(total);

        var n = w * h;
        var ratio = total / n;
        select('#percentWhite').elt.innerText = int(100 * ratio);
    }
    if (!sampling) {
        capture.updatePixels();
    }
  
    //move image by the width of image to the left
  translate(capture.width, 0);
  //then scale it by -1 in the x-axis
  //to flip the image
  scale(-1, 1);

    image(capture, 0, 0, w, h);

    noStroke();
    fill(255);
    // rect(20, 20, 40, 40);

    rect(sumPosition.x-60, sumPosition.y-10, 120, 20);
  
    ellipse(ballX, ballY, r*2, r*2);
    ballX += xspeed;
    ballY += yspeed;
    if (ballX > width - r || ballX < r) {
      xspeed = -xspeed;
    }
    if (ballY > height - r || ballY < r) {
      yspeed = -yspeed;
    }
    if (ballX > sumPosition.x-60 && ballX < sumPosition.x+60){
      if(ballY + 20 >= sumPosition.y-10 && ballY + 20 < sumPosition.y + 5 ){
        yspeed = -yspeed;
        console.log("yes");
      }
      if(ballY - 20 <= sumPosition.y+10 && ballY - 20 > sumPosition.y - 5 ){
        yspeed = -yspeed;
        console.log("yes");
      }
      
    }
}
