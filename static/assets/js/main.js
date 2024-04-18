$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 900) {
            $('#top').fadeIn(); // Показати кнопку з ефектом зникнення
        } else {
            $('#top').fadeOut(); // Приховати кнопку з ефектом зникнення
        }
    });

    // Плавна анімація переміщення до верху сторінки при кліку на кнопку
    $('#top').click(function() {
        $('html, body').animate({ scrollTop: 0 }, 50);
        return false;
    });
});

// Отримуємо всі посилання з класом animate-link
const links = document.querySelectorAll('.header-catalog a');

// Додаємо обробник події для кожного посилання
links.forEach(link => {
    link.addEventListener('mouseenter', () => {
        const bgColor = link.getAttribute('data-bgcolor');
        link.style.setProperty('--bgcolor', bgColor);
        link.classList.add('animate-bg');
    });

    link.addEventListener('mouseleave', () => {
        link.classList.remove('animate-bg');
    });
});

const contacsts = document.getElementById('footer');
const footer = document.querySelector('.footer');

contacsts.addEventListener('click', () => {
    footer.scrollIntoView({ behavior: 'smooth', block: 'start' });
});