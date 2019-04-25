var canvas = document.querySelector('.myCanvas');
var ctx = canvas.getContext('2d');
var startbtn = document.querySelector('.startbtn');
var countdown = document.querySelector('.countdown');
var ctNum = Number(countdown.textContent);
var svgmain = document.querySelector('.svg-main');

var width = canvas.width = window.innerWidth;
var height = canvas.height = window.innerHeight;

window.addEventListener('resize', resizeCanvas, false);

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

startbtn.onclick = function() {
    startbtn.style.opacity = '0';
    startbtn.style.visibility = 'hidden';
    startbtn.style.backgroundColor = 'green';
    startbtn.style.width = '150px';
    startbtn.style.fontSize = '25px';
    ctNum = 3;
    countdownHandler();
    setInterval(countdownHandler, 1000);
}

var countdownInterval = setInterval(countdownHandler, 1000);
var countdownHandler = function(){
    if (ctNum>0) {
    countdown.textContent = ctNum.toString();
    ctNum--;
    } else if (ctNum==0){
        countdown.remove();
        document.getElementById("svgmain").removeAttribute("id");
        setInterval(timerHandler, 10);
        gameStart();
        ctNum--;
    } else if (ctNum==-1) {
        clearInterval(countdownInterval);
    }
}

var bgColor = ['#F70C0C', '#1652F7', '#000000'];
var textColor = {
    red : '#F70C0C', 
    blue : '#1652F7', 
    black : '#000000'
}

var svgtext = document.querySelector('.svgtext');
var btno = document.querySelector('#O');
var btnx = document.querySelector('#X');
var keys = Object.keys(textColor);
function disableBtns() {
    document.querySelector('#O').disabled = true;
    document.querySelector('#X').disabled = true;
}

function enableBtns() {
    document.querySelector('#O').disabled = false;
    document.querySelector('#X').disabled = false;
}

function gameStart() {
    enableBtns();
    btno.style.backgroundColor = '#d8dcdf';
    btnx.style.backgroundColor = '#d8dcdf';
    var randBg = bgColor[Math.floor(Math.random()*bgColor.length)];
    var randTx = bgColor[Math.floor(Math.random()*bgColor.length)];
    var bgresult = canvas.style.backgroundColor = randBg;
    var randomKey = Object.keys(textColor)[Math.floor(Math.random()*keys.length)];
    svgtext.textContent = randomKey.toUpperCase();
    svgtext.style.fill = randTx;
    btno.onclick = function() {
        if (bgresult == textColor[randomKey]){
            btno.style.backgroundColor = 'green';
            getPoint();
        }
        else {
            btno.style.backgroundColor = 'red';
            losePoint();
        }
        disableBtns();
        setTimeout(function(){ gameStart(); }, 300);
    }
    btnx.onclick = function() {
        if (bgresult !== textColor[randomKey]){
            btnx.style.backgroundColor = 'green';
            getPoint();
        }
        else {
            btnx.style.backgroundColor = 'red';
            losePoint();
        }
        disableBtns();
        setTimeout(function(){ gameStart(); }, 300);
    }
}

var score = document.querySelector(".score");

point = 0;
score.textContent = "Score : " + point.toString();

function getPoint() {
    point++;
    return score.textContent = "Score : " + point.toString();
}

function losePoint() {
    point-=2;
    return score.textContent = "Score : " + point.toString();
}

var timer = document.querySelector(".timer");
var timerInterval = setInterval(timerHandler, 10);
var width = 100;

var timerHandler = function() {
    if (width >= 0){
    timer.style.width = width + "%";
    width -= 0.05;
    } else if (width < 0) {
    gameOver();
    clearInterval(timerInterval);
    }
}

var oxBtn = document.querySelector('.OX');
var gameOver = function() {
    disableBtns();
    oxBtn.style.display = 'none';
    restartBtn.style.visibility = 'visible';
}

var restartBtn = document.querySelector('.restart');

restartBtn.onclick = function() {
    window.location.reload();
}