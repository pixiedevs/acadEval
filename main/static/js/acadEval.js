const BodyPr = document.getElementById('inBody');
const toggle = document.getElementById('dark-toggle');
toggle.onclick = function () {
    toggle.classList.toggle('darkmode');
    BodyPr.classList.toggle('darkmode');

    if (BodyPr.classList.contains('darkmode')) { //when the BodyPr has the class 'darkmod' currently
        localStorage.setItem('darkMode', 'enabled'); //store this data if dark mode is on
    }
    else {
        localStorage.setItem('darkMode', 'disabled'); //store this data if dark mode is off
    }
}
if (localStorage.getItem('darkMode') == 'enabled') {
    toggle.classList.toggle('darkmode');
    BodyPr.classList.toggle('darkmode');
}