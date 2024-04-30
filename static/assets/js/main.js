$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 1000) {
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


document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll('.form-check-input');
    const submitButton = document.getElementById('submitButton');

    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            let anyChecked = false;
            checkboxes.forEach(function(checkbox) {
                if (checkbox.checked) {
                    anyChecked = true;
                }
            });
            if (anyChecked) {
                submitButton.style.display = 'block';
            } else {
                submitButton.style.display = 'none';
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const sortOption = document.getElementById('sortOption');
    const sortForm = document.getElementById('sortForm');

    sortOption.addEventListener('change', function() {
        sortForm.submit();
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Знаходимо кнопку для очищення фільтрів за її id
    const clearFiltersButton = document.getElementById('clearFiltersButton');

    // Додаємо обробник подій для натискання кнопки
    clearFiltersButton.addEventListener('click', function() {
        // Встановлюємо новий URL без параметрів запиту
        window.history.replaceState({}, document.title, window.location.pathname);
        // Перезавантажуємо сторінку
        window.location.reload();
    });
});

