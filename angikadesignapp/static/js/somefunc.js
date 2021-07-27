// Top Func 
const myBtn = document.getElementById('myBtn');

window.onscroll = function () { scrollFunction() }

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        myBtn.style.display = "block";
    } else {
        myBtn.style.display = "none";
    }
}

myBtn.addEventListener('click', function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0
})

// CopyRight Year 
const copyrightYear = document.getElementById('copyrightYear');
let date = new Date()
let Year = date.getFullYear()
copyrightYear.innerText = Year