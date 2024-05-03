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
    const sortOption = document.getElementById('sortOption');
    const sortForm = document.getElementById('sortForm');
    const clearFiltersButton = document.getElementById('clearFiltersButton');

    // Обробник події для зміни чекбоксів
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

    // Обробник події для вибору сортування
    sortOption.addEventListener('change', function() {
        sortForm.submit();
    });

    // Обробник події для очищення фільтрів
    clearFiltersButton.addEventListener('click', function() {
        window.history.replaceState({}, document.title, window.location.pathname);
        window.location.reload();
    });

    // Інші обробники подій...
});

// Для форм Авторизації та Реєстрації 

(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {

      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        
        form.classList.add('was-validated');
      }, false)
      
    })
  })()
