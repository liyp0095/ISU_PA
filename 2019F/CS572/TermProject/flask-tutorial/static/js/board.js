var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");

var bd = document.getElementById("board div");
alert(window.innerWidth);

// c.width = window.innerWidth*0.5;
// c.height = window.innerWidth*0.5;

(function() {
    var
    // Obtain a reference to the canvas element using its id.
    htmlCanvas = document.getElementById('myCanvas'),
    // Obtain a graphics context on the canvas element for drawing.
    context = htmlCanvas.getContext('2d');

   // Start listening to resize events and draw canvas.
   initialize();

   function initialize() {
       // Register an event listener to call the resizeCanvas() function
       // each time the window is resized.
       window.addEventListener('resize', resizeCanvas, false);
       // Draw canvas border for the first time.
       resizeCanvas();
    }

    // Display custom canvas. In this case it's a blue, 5 pixel
    // border that resizes along with the browser window.
    function redraw() {
       context.strokeStyle = 'blue';
       context.lineWidth = '10';
       context.strokeRect(0, 0, htmlCanvas.width, htmlCanvas.height);
    }

    // Runs each time the DOM window resize event fires.
    // Resets the canvas dimensions to match window,
    // then draws the new borders accordingly.
    function resizeCanvas() {
        htmlCanvas.width = window.innerWidth*0.1;
        htmlCanvas.height = window.innerHeight*0.1;
        redraw();
    }
})();

// for(i=0;i<8;i++){
//   for(j=0;j<8;j++){
//     ctx.moveTo(0,70*j);
//     ctx.lineTo(560,70*j);
//     ctx.stroke();
//
//     ctx.moveTo(70*i,0);
//     ctx.lineTo(70*i,560);
//     ctx.stroke();
//     var left = 0;
//     for(var a=0;a<8;a++) {
//       for(var b=0; b<8;b+=2) {
//         startX = b * 70;
//         if(a%2==0) startX = (b+1) * 70;
//         ctx.fillRect(startX + left,(a*70) ,70,70);
// 	    }
//     }
//   }
// }
