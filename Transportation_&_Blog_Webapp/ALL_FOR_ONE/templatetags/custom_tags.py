from pickle import TRUE
from django import template

register = template.Library()

@register.simple_tag()
def get_halfContent(postDetail):
    return postDetail[:int(len(postDetail) / 3)]


# @register.simple_tag()
# def ifeqaul(var1, var2):
#     if var1 == var2:
#         return True
#     else: 
#         return False