from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.utils.crypto import get_random_string
import re, string, random, datetime

# Create your views here.
def index(request):



    return render(request, 'first_app/index.html')

def attempt(request):

    if 'attempt_count' not in request.session:
        request.session['attempt_count'] = 0
    else:
        request.session['attempt_count'] += 1
        print request.session['attempt_count']

    allowed_chars = ''.join((string.ascii_letters, string.digits))
    random_word = ''.join(random.choice(allowed_chars) for _ in range(14))
    print random_word
    request.session['random_word'] = get_random_string(length=14)

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')