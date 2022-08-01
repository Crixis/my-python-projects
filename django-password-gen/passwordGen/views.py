from django.shortcuts import render
#from django.http import HttpResponse
import random

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    gen_pass=''

    passlength=int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('-!#*$%@&'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(passlength):
        gen_pass+=random.choice(characters)

    return render(request, 'password.html',{'password':gen_pass})
