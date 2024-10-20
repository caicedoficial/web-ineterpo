document.addEventListener('DOMContentLoaded', function() {
    const carrusel = document.querySelector('.noticia-carrusel');
    if (carrusel) {
        const imagenes = carrusel.querySelectorAll('.noticia-imagen');
        const btnPrev = carrusel.querySelector('.prev');
        const btnNext = carrusel.querySelector('.next');
        let indiceActual = 0;

        function mostrarImagen(indice) {
            imagenes.forEach(img => img.style.display = 'none');
            imagenes[indice].style.display = 'block';
        }

        function siguienteImagen() {
            indiceActual = (indiceActual + 1) % imagenes.length;
            mostrarImagen(indiceActual);
        }

        function imagenAnterior() {
            indiceActual = (indiceActual - 1 + imagenes.length) % imagenes.length;
            mostrarImagen(indiceActual);
        }

        btnPrev.addEventListener('click', imagenAnterior);
        btnNext.addEventListener('click', siguienteImagen);

        // Cambio automático de imagen cada 5 segundos
        setInterval(siguienteImagen, 5000);
    }
});