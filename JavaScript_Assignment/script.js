let screen = document.querySelector("#screen");
let btns = document.querySelectorAll(".btn");
let dark_light = document.querySelector("#theme");
let container = document.querySelector('.container');
let row_theme = document.querySelectorAll('.row_theme');
let theme_text = document.querySelector('#theme_text');
let memory = 0;
console.log(row_theme);

dark_light.addEventListener('click', ()=>{
    dark_light.classList.toggle("dark");
    dark_light.classList.toggle("white");
    document.body.classList.toggle('theme_white');
    document.body.classList.toggle('theme_dark');
    container.classList.toggle('container_dark');
    for (let i = 0; i < row_theme.length; i++) {
        row_theme[i].classList.toggle('row_button');
    }
    if(theme_text.innerText == 'Dark'){
        theme_text.innerText = 'Light';
    }
    else{
        theme_text.innerText = 'Dark';
    }

});
for(btn of btns)
{
    btn.addEventListener('click', (e)=> {
        btntext = e.target.innerText;
        screen.value += btntext;
    })
}

function calculate(){
    screen.value = eval(screen.value)
}

function sin() {
    screen.value = Math.sin(screen.value)
}
function cos() {
    screen.value = Math.cos(screen.value)
}
function tan() {
    screen.value = Math.tan(screen.value)
}
function pow() {
    screen.value = Math.pow(screen.value,2)
}
function sqrt() {
    screen.value = Math.sqrt(screen.value,2)
}
function log() {
    screen.value = Math.log(screen.value) / Math.log(10);
}
function pi(){
    screen.value = 3.14159265359;
}
function e() {
    screen.value = 2.71828182846;
}

function fact() {
    let i, num, f;
    f = 1;
    num = screen.value;
    for (i = 1; i <= num ; i++) {
        f = f * i;
    }
    i = i - 1;
    screen.value = f;
}

function backspace() {
    screen.value = screen.value.substr(0,screen.value.length - 1);
}
function mr() {
    screen.value = memory;
}
function mc() {
    memory = 0;
    screen.value = '';
}
function mplus() {
    memory += eval(screen.value);
    screen.value = '';
}
function mminus() {
    memory -= eval(screen.value);
    screen.value = '';
}