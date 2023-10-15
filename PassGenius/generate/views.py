from django.shortcuts import render

from random import choice
chars = '!&$#?@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate(request):
    template = 'generate/generate.html'
    password = ''
    for i in range(6):
        if i == 3:
            password += str(choice(range(0,9)))
        password += choice(chars)

    context = {
        'password': password
    }

    return render(request, template, context)
