var images = [
    '../slideshow/1.jpg',
    '../slideshow/2.jpg',
    '../slideshow/3.jpg',
    '../slideshow/4.jpg'
]

var num = 0;
console.log(num);

function slideshow() {
    var slide = document.querySelector(".container");
    num++;
    if(num >=images.length) {
        num = 0;
    }
    slide.style.backgroundImage = "url('"+ images[num] + " ')";
    // slide.setAttribute("style", "background-image: url('"+ images[num] + " ')");
    // console.log(document.body.style.backgroundImage);
}


setInterval(slideshow, 3000);

// slideshow(); 