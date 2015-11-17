# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test

from forms import *
from models import *


@login_required()
def index(request):
    context = {}
    return render(request, "index.html", context)


def logout(request):
    try:
        auth_logout(request)
    except:
        pass
    return redirect('login')


def login(request):
    context = {}
    context['msg'] = ""
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        context['username'] = request.POST['username']
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('index')
            else:
                context['msg'] = "Usuário Desabilitado Temporariamente"
        else:
            context['msg'] = "Nome de Usuário e/ou Senha inválidos"
    return render(request, "login.html", context)


@login_required()
def orders(request):
    context = {}
    context['orders'] = Order.objects.all()
    return render(request, "orders.html", context)


@login_required()
def new_order(request):
    context = {}
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm()
    context['form'] = form
    return render(request, "new_order.html", context)


@login_required()
def edit_order(request, id_order):
    context = {}
    try:
        order = Order.objects.get(id=id_order)
    except:
        return redirect('orders')

    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm(instance=order)
    context['form'] = form
    return render(request, "new_order.html", context)


@user_passes_test(lambda u: u.is_superuser)
def rmv_order(request, id_order):
    context = {}
    try:
        order = Order.objects.get(id=id_order)
        order.delete()
        return redirect('orders')
    except:
        return redirect('orders')


@login_required()
def clients(request):
    context = {}
    context['clients'] = Client.objects.all()
    return render(request, "clients.html", context)


@login_required()
def new_client(request):
    context = {}
    if request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientForm()
    context['form'] = form
    return render(request, "new_client.html", context)


@login_required()
def edit_client(request, id_client):
    context = {}

    try:
        client = Client.objects.get(id=id_client)
    except:
        return redirect('clients')

    if request.POST:
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientForm(instance=client)
    context['form'] = form
    return render(request, "new_client.html", context)


@user_passes_test(lambda u: u.is_superuser)
def rmv_client(request, id_client):
    context = {}
    try:
        client = Client.objects.get(id=id_client)
        client.delete()
        return redirect('clients')
    except:
        return redirect('clients')


@user_passes_test(lambda u: u.is_superuser)
def billing(request):
    context = {}
    return render(request, "billing.html", context)


@login_required()
def products(request):
    context = {}
    context['products'] = Product.objects.all()
    return render(request, "products.html", context)


@login_required()
def new_product(request):
    context = {}
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    context['form'] = form
    return render(request, "new_product.html", context)


@login_required()
def edit_product(request, id_product):
    context = {}
    try:
        product = Product.objects.get(id=id_product)
    except:
        return redirect('products')

    if request.POST:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    context['form'] = form
    return render(request, "new_product.html", context)


@user_passes_test(lambda u: u.is_superuser)
def rmv_product(request, id_product):
    context = {}
    try:
        product = Product.objects.get(id=id_product)
        product.delete()
        return redirect('products')
    except:
        return redirect('products')