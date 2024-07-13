// 1) Navbar Scroll Down Animation
let lastScrollTop = 0;
const navbar = document.querySelector('.header .main-navbar');
let navbarHeight = navbar.clientHeight;

window.addEventListener('scroll', function() {
  let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > lastScrollTop && scrollTop > navbarHeight) {
    // Scroll down
    navbar.classList.add('hidden-nav');
  } else {
    // Scroll up
    navbar.classList.remove('hidden-nav');
  }

  // Check if scroll position is at the top
  if (scrollTop === 0) {
    navbar.classList.remove('scroll-up'); // Remove background color class
  } else {
    navbar.classList.add('scroll-up'); // Add background color class
  }

  lastScrollTop = scrollTop; // Update last scroll position
}, false);



// 2) Navbar Side Navigation Animation
function menuAnimation(x) {
    x.classList.toggle("change");
    var element = document.getElementById("slideNav");
    element.classList.toggle("navSlide");
    var textFade = document.getElementById("sideBarText");
    textFade.classList.toggle("textFadeIn");
    var iconFade = document.getElementById("socialIcons");
    iconFade.classList.toggle("iconFadeIn");
  }






// 3) Booking Schedule Content Form Date Display
   function showDatepicker(input) {
    input.type = 'date';
    input.focus();
}

    // Handle focus events to manage placeholder display
document.addEventListener('DOMContentLoaded', function() {
    const dateInputs = document.querySelectorAll('.date-input');
    dateInputs.forEach(input => {
        const defaultPlaceholder = input.placeholder;
        input.addEventListener('focus', function() {
            this.placeholder = '';
            this.type = 'date'; // Ensure input type remains 'date' on focus
        });
        input.addEventListener('blur', function() {
            if (!this.value) {
                this.placeholder = defaultPlaceholder;
                this.type = 'text'; // Reset to text input type if no date selected
            }
        });
    });
});













// 4) Driving Excellence Slider
var options = {
  wrapAround: true, // Enable looping
  prevNextButtons: false,
  accessibility: true,
  pageDots: true,
  setGallerySize: false,
  arrowShape: {
    x0: 10,
    x1: 60,
    y1: 50,
    x2: 60,
    y2: 45,
    x3: 15
  }
};

var carousel = document.querySelector('[data-carousel]');
var slides = document.getElementsByClassName('carousel-cell');
var flkty = new Flickity(carousel, options);


flkty.on('scroll', function () {
  flkty.slides.forEach(function (slide, i) {
    var image = slides[i];
    var x = (slide.target + flkty.x) * -1/3;
    image.style.backgroundPosition = x + 'px center';
  });
});

setInterval(function() {
  flkty.next();
}, 6000); // 3000 milliseconds = 3 seconds