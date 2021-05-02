const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");

let w = canvas.width = window.innerWidth;
let h = canvas.height = window.innerHeight;
let cols = Math.floor(w / 20) + 1;
let ypos = Array(cols).fill(0);
resize_canvas();

var Matrix=function(){
  ctx.fillStyle='rgba(0,0,0,.05)';
  ctx.fillRect(0,0,window.innerWidth,window.innerHeight);

  ctx.fillStyle = 'rgb(0, 255, 0, 0.3)';
  ctx.font = '15pt monospace';

  ypos.forEach((y, ind) => {
      const text = String.fromCharCode(Math.random() * 128);
      const x = ind * 20;
      ctx.fillText(text, x, y);
      if (y > 100 + Math.random() * 10000) ypos[ind] = 0;
      else ypos[ind] = y + 20;
  });
};
setInterval(Matrix,50);


function resize_canvas(){
  if (canvas.width  < window.innerWidth) {
    w = canvas.width = window.innerWidth;
  }
  if (canvas.height < window.innerHeight) {
    h = canvas.height = window.innerHeight;
  }
  cols = Math.floor(w / 20) + 1;
  ypos = Array(cols).fill(0);
}
