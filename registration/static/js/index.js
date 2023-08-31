document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        let preloader = document.querySelector(".preloader");
        let content = document.querySelector(".content");

        preloader.style.display = "none";
        content.style.display = "flex";
    }, 4000); 
});


function hideMessages() {
        const messages = document.querySelectorAll('.message');
        messages.forEach(message => {
            setTimeout(() => {
                message.style.display = 'none';
            }, 5000);
        });
    }

    // Call the hideMessages function when the page loads
window.addEventListener('load', hideMessages);

const form = document.getElementById('art_form');
const submitButton = document.getElementById('btn');

form.addEventListener('submit', function() {
    submitButton.disabled = true;
    submitButton.style.cursor = 'not-allowed';
    submitButton.innerText = "Please wait....";
    // console.log("clicked");

});

let Btn = document.getElementById('btn');
Btn.addEventListener('click', function(){
let slider_one = document.getElementById('slide1');
slider_one.classList.add('slide_show');
});
// let nav = document.querySelector('nav');
// let logo = document.getElementById('logo');
// window.addEventListener('scroll', ()=>{
//     if(window.scrollY > 100){
//         nav.classList.add('scrolled');
//         logo.src = "{% static '../asset/artention-solo.jpg'%}";
//         logo.style.transform = 'scale(1.2)';
//     }else{
//         nav.classList.remove('scrolled');
//         logo.src = "{% static '../asset/artention_logo.png'%}";
//         logo.style.transform = 'scale(1)';
//     }
// })