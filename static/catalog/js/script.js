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
    setTimeout(function() {
        document.querySelector(".loader-wrapper").style.display = "none";
        document.querySelector("#content").style.display = "block";
    }, 2000); 

    // p5.js code
    new p5(function(sketch) {
        sketch.setup = function() {
            let canvas = sketch.createCanvas(sketch.windowWidth, sketch.windowHeight);
            canvas.parent('p5-canvas');
        }

        sketch.draw = function() {
            let x = sketch.random(sketch.width);
            let y = sketch.random(sketch.height);
            let r = sketch.random(255);
            let g = sketch.random(255);
            let b = sketch.random(255);
            sketch.noStroke();
            sketch.fill(r, g, b, 100);
            sketch.ellipse(x, y, 4, 4); 
        }
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
const slides = Array.from(track.children);

// Set the left position of each slide
slides.forEach((slide, index) => {
    slide.style.left = slide.getBoundingClientRect().width * index + 'px';
});

// Move to next slide every 3 seconds
setInterval(() => {
    const currentSlide = track.querySelector('.current-slide');
    const nextSlide = currentSlide.nextElementSibling || slides[0];
    
    // Move to the next slide
    const slideWidth = currentSlide.getBoundingClientRect().width;
    track.style.transform = 'translateX(-' + nextSlide.style.left + ')';
    currentSlide.classList.remove('current-slide');
    nextSlide.classList.add('current-slide');
}, 3000);

// PRODUCTS PAGE scripts
window.onload = function() {
    // Select all product images
    const productImages = document.querySelectorAll('.product-image');

    // Add event listeners to each image
    productImages.forEach(image => {
        image.addEventListener('mouseover', magnify);
        image.addEventListener('mouseout', demagnify);
    });

    // Function to magnify image
    function magnify(e) {
        e.target.style.transform = 'scale(1.2)';
        e.target.style.transition = 'transform 0.3s ease';
    }

    // Function to demagnify image
    function demagnify(e) {
        e.target.style.transform = 'scale(1)';
        e.target.style.transition = 'transform 0.3s ease';
    }
}

// Stripe Js payment form 
// To use this payment method live, you must switch to HTTPs to ensure secure data transfer

var stripe = Stripe('pk_test_51Own3jFlpTEzDIrEWgl8A3ChU9v5tddxPbVh8VTxHJJHAXU0nzAVBRGGvap56gncNJuVudSf0uixGMrU77It6sUV00qCFkadDE');
var elements = stripe.elements();

var card = elements.create('card');

// Check if #card-element exists before mounting
if (document.querySelector('#card-element')) {
    card.mount('#card-element');
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
                stripeTokenHandler(result.token);
            }
        });
    });
}

// Submit Stripe form to Django

function stripeTokenHandler(token) {
    var form = document.getElementById('payment-form');
    if (form) {
        var hiddenInput = document.createElement('input');
        hiddenInput.setAttribute('type', 'hidden');
        hiddenInput.setAttribute('name', 'stripeToken');
        hiddenInput.setAttribute('value', token.id);
        form.appendChild(hiddenInput);

        form.submit();
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
}




console.log("JavaScript is being loaded!");