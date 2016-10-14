from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random

# Create your views here.
def index(request):
    attmpt = request.session.get('hit')
    if not attmpt:
        request.session['hit'] = 1
    else:
        request.session['hit'] += 1
    if request.session['hit'] <= 1 :
        request.session['log'] = []
        request.session['state'] = None
        request.session['time'] = None
        request.session['gold'] = 0
        request.session['delta'] = 0
        request.session['building']= None
    return render(request, 'ninjGld/index.html')

def reset(request):
    request.session['log'] = []
    request.session['state'] = None
    request.session['building'] = None
    request.session['gold'] = 0
    request.session['hit'] = 1
    return redirect('/')

def process_money(request):
    request.session['state'] = 'process_money'
    if request.POST['building'] == 'farm':
        print('farm')
        request.session['delta'] = random.randint(10,20)
        print("gold delta",request.session['delta'])
        request.session['gold'] += request.session['delta']
        print("gold",request.session['gold'])
        request.session['building'] = 'farm'
    elif request.POST['building'] == 'cave':
        print('cave')
        request.session['delta'] = random.randint(5,10)
        print("gold delta",request.session['delta'])
        request.session['gold'] += request.session['delta']
        print("gold",request.session['gold'])
        request.session['building'] = 'cave'
    elif request.POST['building'] == 'house':
        print('house')
        request.session['delta'] = random.randint(2,5)
        print("gold delta",request.session['delta'])
        request.session['gold'] += request.session['delta']
        print("gold",request.session['gold'])
        request.session['building'] = 'house'
    elif request.POST['building'] == 'casino':
        print('casino')
        request.session['delta'] = random.randint(-50,50)
        print("gold delta",request.session['delta'])
        request.session['gold'] += request.session['delta']
        print("gold",request.session['gold'])
        request.session['building'] = 'casino'
    request.session['time'] = str(datetime.now())
    print(request.session['time'])
    print("log pre-append: ", request.session['log'])
    request.session['log'].append((request.session['building'],request.session['delta'],request.session['time']))
    print("log post-append: ", request.session['log'])
    return redirect('/')
