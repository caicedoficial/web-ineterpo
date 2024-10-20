document.addEventListener('DOMContentLoaded', function() {
    const alianzasCarousel = document.querySelector('.alianzas-carousel');
    const logosContainer = alianzasCarousel.querySelector('.alianzas-logos');
    const alianzaLinks = logosContainer.querySelectorAll('.alianza-link');
    let currentIndex = 0;
    let intervalId;

    function showLogo(index) {
        logosContainer.style.transform = `translateX(-${index * 100}%)`;
    }

    function rotateLogos() {
        currentIndex = (currentIndex + 1) % alianzaLinks.length;
        showLogo(currentIndex);
    }

    function startAutoRotation() {
        intervalId = setInterval(rotateLogos, 3000);
    }

    function stopAutoRotation() {
        clearInterval(intervalId);
    }

    // Configurar el contenedor de logos
    logosContainer.style.display = 'flex';
    logosContainer.style.transition = 'transform 0.5s ease-in-out';
    logosContainer.style.width = `${alianzaLinks.length * 100}%`;

    // Configurar cada enlace de logo
    alianzaLinks.forEach(link => {
        link.style.flex = '0 0 100%';
        link.style.width = '100%';
        link.style.height = '100%';
    });

    // Mostrar el primer logo
    showLogo(currentIndex);

    // Iniciar rotación automática
    startAutoRotation();

    // Detener rotación al pasar el mouse por encima
    alianzasCarousel.addEventListener('mouseenter', stopAutoRotation);
    alianzasCarousel.addEventListener('mouseleave', startAutoRotation);
});