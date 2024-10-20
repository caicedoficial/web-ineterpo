document.addEventListener('DOMContentLoaded', function() {
    const contenedor = document.querySelector('.objeto-galeria__contenedor');
    const botonIzquierda = document.querySelector('.carrusel-boton--izquierda');
    const botonDerecha = document.querySelector('.carrusel-boton--derecha');
    let indiceActual = 0;
    const imagenes = contenedor.querySelectorAll('.objeto-galeria__item');
    const totalImagenes = imagenes.length;

    function actualizarCarrusel() {
        contenedor.style.transform = `translateX(-${indiceActual * 100}%)`;
    }

    function moverIzquierda() {
        indiceActual = (indiceActual - 1 + totalImagenes) % totalImagenes;
        actualizarCarrusel();
    }

    function moverDerecha() {
        indiceActual = (indiceActual + 1) % totalImagenes;
        actualizarCarrusel();
    }

    botonIzquierda.addEventListener('click', moverIzquierda);
    botonDerecha.addEventListener('click', moverDerecha);

    actualizarCarrusel();
});