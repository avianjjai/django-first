import string
from .models import bitly
from random import choice
def shortcode_gen():
    code = ""
    chars = string.ascii_uppercase+string.ascii_lowercase+string.digits
    for _ in range(6):
        code += choice(chars)
    return code

def create_Sortcode():
    code = shortcode_gen()
    qs = bitly.objects.filter(shortcode__iexact = code)
    if qs.exists():
        return create_Sortcode()
    return code




    