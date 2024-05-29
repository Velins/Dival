$(document).ready(function() {
    
    var successMessage =  $("#jq-notification");

    $(document).on("click", ".add-to-card", function (e) {
        
        e.preventDefault();

        var productsInCartCount = $("#products-in-cart-count");
        var cartCount = parseInt(productsInCartCount.text() || 0);

        var product_id = $(this).data("product-id");

        var add_to_cart_url = $(this).attr("href");

        $.ajax({
            type : "POST",
            url : add_to_cart_url,
            data :{
                product_id : product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data){
                successMessage.html(data.message);
                successMessage.fadeIn(400);

                setTimeout(function (){
                    successMessage.fadeOut(400);
                }, 2000);

                cartCount++;
                productsInCartCount.text(cartCount);

                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
                
            },

            error: function (data) {
                console.log("Помилка додавння товару в корзину !");
            },
        })
    });
    

    $(document).on("click", ".remove-from-cart", function (e) {

        e.preventDefault();

        var productsInCartCount = $("#products-in-cart-count");
        var cartCount = parseInt(productsInCartCount.text() || 0);

        var cart_id = $(this).data("cart-id");

        var remove_from_cart = $(this).attr("href");

        $.ajax({

            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val()
            },
            success: function (data) {

                successMessage.html(data.message);
                successMessage.fadeIn(400);

                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 2000);

                cartCount -= data.quantity_deleted;
                productsInCartCount.text(cartCount);

                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);  // Змінюємо вміст контейнера
            },

            error: function (data) {
                console.log("Помилка додавання товару в корзину !");
            },
        });
    });

    $(document).on("click", ".decrement", function () {

        var url = $(this).data("cart-change-url");

        var cartID = $(this).data("cart-id");

        var $input = $(this).closest('.ch-qty').find('.quantity');

        var currentValue = parseInt($input.text());

        if (currentValue > 1) {
            $input.val(currentValue - 1);

            updateCart(cartID, currentValue - 1, -1, url);
        }
    });
    
    $(document).on("click", ".increment", function () {

        var url = $(this).data("cart-change-url");

        var cartID = $(this).data("cart-id");

        var $input = $(this).closest('.ch-qty').find('.quantity');

        var currentValue = parseInt($input.text());

        $input.val(currentValue + 1);


        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {

                successMessage.html(data.message);
                successMessage.fadeIn(400);

                setTimeout(function () {
                     successMessage.fadeOut(400);
                }, 2000);


                var productsInCartCount = $("#products-in-cart-count");
                var cartCount = parseInt(productsInCartCount.text() || 0);
                cartCount += change;
                productsInCartCount.text(cartCount);

                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("Помилка додавання товару в корзину !");
            },
        });
    }
});


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

    var notifictaion = $('#notification')

    if (notifictaion.length > 0)
            {setTimeout(function (){
                notifictaion.fadeOut();
            }, 2000)
            setTimeout(function (){
                notifictaion.alert('close');
            }, 2300)
        }

    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $(".address input").attr("required", true);
            $(".address").show();
        } else {
            $(".address input").removeAttr("required");
            $(".address").hide();
        }
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

const contacts = document.getElementById('footer');
const footer = document.querySelector('.footer');

if (contacts && footer) {
contacts.addEventListener('click', () => {
    footer.scrollIntoView({ behavior: 'smooth', block: 'start' });
})};


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

    if (sortOption) {
    // Обробник події для вибору сортування
    sortOption.addEventListener('change', function() {
        sortForm.submit();
    });
    }

    const hasFilters = window.location.search.includes('color') || window.location.search.includes('material') || window.location.search.includes('style') || window.location.search.includes('sort_option');
    
    if (hasFilters) {
        // Якщо є параметри, показуємо кнопку "Очистити"
        clearFiltersButton.style.display = 'block';
    } else {
        // Якщо немає параметрів, ховаємо кнопку "Очистити"
        clearFiltersButton.style.display = 'none';
    }
    
    if (clearFiltersButton) {
    // Обробник події для очищення фільтрів
    clearFiltersButton.addEventListener('click', function() {
        window.history.replaceState({}, document.title, window.location.pathname);
        window.location.reload();
    });
    }

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

// Маска телефону укр. формату 
const element = document.getElementById('id_phone');
if (element) {
    const maskOptions = {
        mask: '+{38}(000)000-00-00',
        lazy: false
      };
    const mask = IMask(element, maskOptions);
}

    const maxLength = 20; // Максимальна кількість символів перед скороченням
    const elements = document.querySelectorAll(".product-order-name");

    elements.forEach(element => {
        const originalText = element.textContent;
        if (originalText.length > maxLength) {
        const truncatedText = originalText.slice(0, maxLength) + "...";
        element.textContent = truncatedText;
        }
  });