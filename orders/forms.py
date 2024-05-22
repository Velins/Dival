import re
from django import forms


class CreateOrderForm(forms.Form):
    OPERATORS_CODES = ['50', '66', '67', '68', '96', '97', '98', '99']  # Коди операторів

    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
            ],
        )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
            ],
        )

    city = forms.CharField(required=False)
    street = forms.CharField(required=False)
    building = forms.CharField(required=False)
    apartment = forms.CharField(required=False)

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        digits_only_phone = re.sub(r'\D', '', phone)  # Видалити всі нецифрові символи
        if len(digits_only_phone) != 12:
            raise forms.ValidationError("Номер телефону повинен містити 10 цифр")
        
        # Перевірка на належність до кодів операторів
        operator_code = phone[5:7]
        if operator_code not in self.OPERATORS_CODES:
            raise forms.ValidationError("Непідтримуваний оператор мобільного зв'язку")

        return phone
    
    def clean(self):
        cleaned_data = super().clean()
        requires_delivery = cleaned_data.get('requires_delivery') == '1'

        city = cleaned_data.get('city')
        street = cleaned_data.get('street')
        building = cleaned_data.get('building')
        apartment = cleaned_data.get('apartment')

        if requires_delivery and (not city or not street or not building):
            raise forms.ValidationError("Для адресної доставки всі поля адреси мають бути заповнені !")

        if city and street and building:
            address = f"{city}, {street}, буд. {building}"
            if apartment:
                address += f", кв. {apartment}"
            cleaned_data['delivery_address'] = address

        return cleaned_data
