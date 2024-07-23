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



// 5) Counter

$('.counter').counterUp({
    delay: 10,
    time: 2000
  });
  $('h3').addClass('animated fadeIn');



// 6) Card Slider


$('.owl-carousel-1').owlCarousel({
  loop: false,
  nav:false,
  margin:20,
  autoplay: false,
  responsive:{
      0:{
          items:1
      },
      600:{
          items:2
      },
      1000:{
          items:3
      }
  }
})





// 7) Rating
$(':radio').change(function() {
  console.log('New star rating: ' + this.value);
});



// 8 what customers say about carent )

$('.owl-carousel-2').owlCarousel({
  loop: true,
  nav:false,
  margin:20,
  autoplay: true,
  responsive:{
      0:{
          items:1
      },
      600:{
          items:1
      },
      1000:{
          items:1
      }
  }
})



// 9 OUR LATEST BLOG & ARTICLES)

$('.owl-carousel-3').owlCarousel({
  loop: false,
  nav:false,
  margin:20,
  autoplay: false,
  responsive:{
      0:{
          items:1
      },
      600:{
          items:2
      },
      1000:{
          items:3
      }
  }
})





// 10 GENERAL QUESTIONS)

const items = document.querySelectorAll(".accordion button");

function toggleAccordion() {
  const itemToggle = this.getAttribute('aria-expanded');
  
  for (i = 0; i < items.length; i++) {
    items[i].setAttribute('aria-expanded', 'false');
  }
  
  if (itemToggle == 'false') {
    this.setAttribute('aria-expanded', 'true');
  }
}

items.forEach(item => item.addEventListener('click', toggleAccordion));





// Page OUR CARS)

// 1) Card Slider)




$('.owl-carousel-6').owlCarousel({
  loop: false,
  nav:false,
  margin:20,
  autoplay: false,
  responsive:{
      0:{
          items:1
      },
      600:{
          items:2
      },
      1000:{
          items:3
      }
  }
})



// Page CAR DETAIL)


$('.owl-carousel-7').owlCarousel({
  loop: true,
  nav:false,
  dots:false,
  margin:20,
  autoplay: true,
  responsive:{
      0:{
          items:1
      },
      600:{
          items:2
      },
      1000:{
          items:3
      }
  }
})






// Page CONTACT)

$(document).ready(function(){

	//material contact form
	$('.contact-form').find('.form-control').each(function() {
	  var targetItem = $(this).parent();
	  if ($(this).val()) {
		$(targetItem).find('label').css({
		  'top': '10px',
		  'fontSize': '14px'
		});
	  }
	})
	$('.contact-form').find('.form-control').focus(function() {
	  $(this).parent('.input-block').addClass('focus');
	  $(this).parent().find('label').animate({
		'top': '10px',
		'fontSize': '14px'
	  }, 300);
	})
	$('.contact-form').find('.form-control').blur(function() {
	  if ($(this).val().length == 0) {
		$(this).parent('.input-block').removeClass('focus');
		$(this).parent().find('label').animate({
		  'top': '25px',
		  'fontSize': '18px'
		}, 300);
	  }
	})
	
});