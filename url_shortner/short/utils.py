import string
from .models import Bitly
from random import choice
from bs4 import BeautifulSoup as soup
import requests

def gettitle(url):
    page = requests.get(url)
    page = soup(page.content,"html.parser")
    title = page.find_all("title")[0]
    title = title.text
    return title


def shortcode_gen():
    code = ""
    chars = string.ascii_uppercase+string.ascii_lowercase+string.digits
    for _ in range(6):
        code += choice(chars)
    return code

def create_Sortcode():
    code = shortcode_gen()
    qs = Bitly.objects.filter(shortcode__iexact = code)
    if qs.exists():
        return create_Sortcode()
    return code