var ans = 0;

function addition() {
    let a = document.getElementById('inp1').value;
    let b = document.getElementById("inp2").value;
    ans = parseInt(a) + parseInt(b);
}

function subtraction() {
    let a = document.getElementById('inp1').value;
    let b = document.getElementById("inp2").value;
    ans = parseInt(a) - parseInt(b);
}

function multiplication() {
    let a = document.getElementById('inp1').value;
    let b = document.getElementById("inp2").value;
    ans = parseInt(a) * parseInt(b);
}

function division() {
    let a = document.getElementById('inp1').value;
    let b = document.getElementById("inp2").value;
    ans = parseInt(a) / parseInt(b);
}


function submit() {
    alert("The Result is " + ans);
}