function setup() {
    createCanvas(windowWidth, windowHeight, WEBGL);
  }
  
  function draw() {
    background(0);
    noFill();
    stroke(200, 200, 100);
    translate(-windowWidth/2+50, -windowHeight/2+30, 0);
    for (let i = 1; i < int(windowHeight/95); i++) {
        push();
        translate(0,90*i);
        for (let j = 1; j < int(windowWidth/95); j++) {
            translate(90,0);
            push(); // Start a new drawing state
            if(i%3 === 0){
                if(j%3 === 0){
                    rotateZ(frameCount * 0.01);
                    rotateX(frameCount * 0.01);
                    rotateY(frameCount * 0.01);
                }
                if(j%3 === 1){
                    rotateZ(frameCount * -0.01);
                    rotateX(frameCount * 0.01);
                    rotateY(frameCount * 0.01);
                }
                else{
                    rotateZ(frameCount * -0.01);
                    rotateX(frameCount * -0.01);
                    rotateY(frameCount * 0.01);
                }
            }
            else if(i%3 === 1){
                if(j%3 === 1){
                    rotateZ(frameCount * 0.01);
                    rotateX(frameCount * 0.01);
                    rotateY(frameCount * 0.01);
                }
                if(j%3 === 2){
                    rotateZ(frameCount * -0.01);
                    rotateX(frameCount * 0.01);
                    rotateY(frameCount * 0.01);
                }
                else{
                    rotateZ(frameCount * -0.01);
                    rotateX(frameCount * -0.01);
                    rotateY(frameCount * 0.01);
                }
            }
            else{
                if(j%3 === 2){
                    rotateZ(frameCount * 0.01);
                    rotateX(frameCount * 0.01);
                    rotateY(frameCount * 0.01);
                }
                if(j%3 === 0){
                    rotateZ(frameCount * -0.01);
                    rotateX(frameCount * 0.01);
                    rotateY(frameCount * 0.01);
                }
                else{
                    rotateZ(frameCount * -0.01);
                    rotateX(frameCount * -0.01);
                    rotateY(frameCount * 0.01);
                }
            }
            box(25,25,25);
            pop(); // Restore original state so that each box rotates around its own center
          }
        pop();
    } 
  }
