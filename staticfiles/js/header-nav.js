document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.getElementById('menu-btn');
    const navMenu = document.getElementById('nav-menu');

    menuBtn.addEventListener('click', () => {
        navMenu.classList.toggle('translate-y-full');
        navMenu.classList.toggle('opacity-0');
    });

    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth < 1024) {
                navMenu.classList.add('translate-y-full');
                navMenu.classList.add('opacity-0');
            }
        });
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth >= 1024) {
            navMenu.classList.remove('translate-y-full');
            navMenu.classList.remove('opacity-0');
        } else {
            navMenu.classList.add('translate-y-full');
            navMenu.classList.add('opacity-0');
        }
    });
});