# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'store/index.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def buy(request):
    if request.session.get('total_items') == None:
        request.session['total_items'] = 0
    if request.session.get('total_cost') == None:
        request.session['total_cost'] = 0

    prices = {
        "1": "29.99",
        "2": "49.99",
        "3": "59.99",
        "4": "49.99"
    }
    request.session['product_id'] = request.POST['id']
    request.session['price'] = prices[request.POST['id']]
    request.session['qty'] = request.POST['qty']
    request.session['total'] = float(prices[request.POST['id']]) * int(request.POST['qty'])
    request.session['total_items'] += int(request.POST['qty'])
    request.session['total_cost'] += float(prices[request.POST['id']]) * int(request.POST['qty'])
    return redirect('/amadon/checkout')

def back(request):
    request.session.pop('product_id')
    request.session.pop('price')
    request.session.pop('qty')
    request.session.pop('total')
    return redirect('/')
