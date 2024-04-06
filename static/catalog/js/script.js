// code for particles.js background
window.addEventListener('load', function() {
    if (typeof particlesJS !== 'undefined') {
        // Existing particles.js instance
        particlesJS.load('particles-js', particlesJsonUrl, function() {
            console.log('particles.js loaded - callback');
        });
    }
});

// code for page wrapper
document.addEventListener("DOMContentLoaded", function() {
    let loaderWrapper = document.querySelector(".loader-wrapper");
    let content = document.querySelector("#content");
    if (loaderWrapper && content) {
        loaderWrapper.style.display = "block";
        content.style.display = "none";
        setTimeout(function() {
            loaderWrapper.style.display = "none";
            content.style.display = "block";
        }, 2000); 
    }

    // p5.js code
    if (typeof p5 !== 'undefined') {
        new p5(function(sketch) {
            sketch.setup = function() {
                let canvas = sketch.createCanvas(sketch.windowWidth, sketch.windowHeight);
                canvas.parent('p5-canvas');
                sketch.background(0); 
            };
    
            sketch.draw = function() {
                let x = sketch.random(sketch.width);
                let y = sketch.random(sketch.height);
                sketch.noStroke();
                sketch.fill(255); 
                sketch.ellipse(x, y, 2, 2); 
            };
        });
    }
});

// nav menu js 
$(document).ready(function() {
    // Function to expand elements on hover
    $('nav ul li').hover(function() {
        $(this).css('flex-grow', 3);
        $(this).siblings().css('flex-grow', 1);
    });
});

// nav menu js 

$(document).ready(function() {
    // Function to expand elements on hover
    $('nav ul li').hover(function() {
        $(this).css('flex-grow', 3);
        $(this).siblings().css('flex-grow', 1);
    });
});



// Header image pulsating effect
const header = document.querySelector('.site-header');
const featuredProducts = document.querySelector('.featured-products');
let brightness = 1;

setInterval(() => {
    brightness = brightness === 1 ? 1.5 : 1;
    if (header) {
        header.style.filter = `brightness(${brightness})`;
    }
    if (featuredProducts) {
        featuredProducts.style.filter = `brightness(${brightness})`;
    }
}, 2000);


// code for index carousel
const track = document.querySelector('.carousel__track');
let slides;
if (track) {
    slides = Array.from(track.children);
    // Set the left position of each slide
    slides.forEach((slide, index) => {
        slide.style.left = slide.getBoundingClientRect().width * index + 'px';
    });
} else {
    console.error('Element with class "carousel__track" not found');
}

// Move to next slide every 3 seconds
if (slides) {
    setInterval(() => {
        const currentSlide = track.querySelector('.current-slide');
        const nextSlide = currentSlide.nextElementSibling || slides[0];
        
        // Move to the next slide
        const slideWidth = currentSlide.getBoundingClientRect().width;
        track.style.transform = 'translateX(-' + nextSlide.style.left + ')';
        currentSlide.classList.remove('current-slide');
        nextSlide.classList.add('current-slide');
    }, 3000);
}
// PRODUCTS PAGE scripts


var stripe = Stripe('pk_test_51P2JooHuzaSV1vlk5q623torJaeFTAdDNIHcrdYGi3uOoDr7fpWZFXzG1nGDA8V2q8SMinS9u3r1b3E6kQVw2nqw00p8N0YEYa');
var elements = stripe.elements();

var card = elements.create('card');

// Check if #card-element exists before mounting
var cardElement = document.querySelector('#card-element');
if (cardElement) {
    card.mount('#card-element');
} else {
    console.error('Element with id "card-element" not found');
}

var form = document.getElementById('payment-form');
if (form) {
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        stripe.createToken(card).then(function(result) {
            if (result.error) {
                var errorElement = document.getElementById('card-errors');
                errorElement.textContent = result.error.message;
            } else {
                console.log('Token created:', result.token.id);  // Log the token ID
                stripeTokenHandler(result.token);
            }
        });
    });
} else {
    console.error('Element with id "payment-form" not found');
}

function stripeTokenHandler(token) {
    var form = document.getElementById('payment-form');
    if (form) {
        var hiddenInput = document.createElement('input');
        hiddenInput.setAttribute('type', 'hidden');
        hiddenInput.setAttribute('name', 'stripeToken');
        hiddenInput.setAttribute('value', token.id);
        form.appendChild(hiddenInput);

        console.log('Form submitted with token:', token.id);  // Log the token ID
        form.submit();
    } else {
        console.error('Element with id "payment-form" not found');
    }
}
// Validate review rating field max value 10 REVIEWS PAGE FORM

window.onload = function() {
    var reviewForm = document.getElementById('reviewForm');
    if (reviewForm) {
        reviewForm.addEventListener('submit', function(event) {
            var rating = document.getElementById('rating').value;
            if (rating < 1 || rating > 10) {
                alert('Rating must be between 1 and 10.');
                event.preventDefault();
            }
        });
    }
};

// Dashboard Scripts 


console.log("JavaScript is being loaded!");