from django.shortcuts import render
import random
import string

# Create your views here.
def code_generator(size=6, char=string.ascii_lowercase + string.digits + string.ascii_uppercase):
    return ''.join(random.choice(char) for i in range(size))
