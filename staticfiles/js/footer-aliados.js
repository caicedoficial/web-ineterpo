document.addEventListener('DOMContentLoaded', function() {
    const aliadosContainer = document.querySelector('#aliados-container');
    const links = aliadosContainer.querySelectorAll('#aliados-link');
    let currentIndex = 0;
    let intervalId;

    function showLogo(index) {
        links.forEach(link => {
            link.style.transform = `translateX(-${index * 100}%)`;
            link.style.transition = 'transform 0.5s ease-in-out';
        });
    }

    function rotateLogos() {
        currentIndex = (currentIndex + 1) % links.length;
        showLogo(currentIndex);
    }

    function startAutoRotation() {
        intervalId = setInterval(rotateLogos, 3000);
    }

    function stopAutoRotation() {
        clearInterval(intervalId);
    }

    // Mostrar el primer logo
    showLogo(currentIndex);

    // Iniciar rotación automática
    startAutoRotation();

    // Detener rotación al pasar el mouse por encima
    aliadosContainer.addEventListener('mouseenter', stopAutoRotation);
    aliadosContainer.addEventListener('mouseleave', startAutoRotation);
});