from django import template
from django.utils.http import urlencode
from products.models import Category
from users.forms import UserLoginForm

register = template.Library()

@register.simple_tag()
def tag_category():
    return Category.objects.all().order_by('id')

@register.simple_tag(takes_context=True)
def change_params(context,**kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

