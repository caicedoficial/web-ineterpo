document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('carousel');
    if (!carousel) return; // Exit if no carousel is found

    let currentSlide = 0;
    const slides = carousel.children;
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    
    // Hide navigation buttons if there's only one image
    if (slides.length <= 1) {
        prevBtn.style.display = 'none';
        nextBtn.style.display = 'none';
        return;
    }
    
    function moveCarousel(direction) {
        currentSlide = (currentSlide + direction + slides.length) % slides.length;
        updateCarousel();
    }
    
    function updateCarousel() {
        carousel.style.transform = `translateX(-${currentSlide * 100}%)`;
    }

    // Add event listeners to buttons
    prevBtn.addEventListener('click', () => moveCarousel(-1));
    nextBtn.addEventListener('click', () => moveCarousel(1));
});