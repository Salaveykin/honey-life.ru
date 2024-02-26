from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def news(request):
    return render(request, 'main/news.html')

def home(request):
    return render(request, 'main/home.html')

def about_us(request):
    return render(request, 'main/about-us.html')

def indexItems(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {
        'item':item
    }
    return render(request, 'main/detail.html', context)

def catalog(request):
    page_obj = items = Product.objects.all()

    item_name = request.GET.get('search')
    if item_name != '' and item_name is not None:
        page_obj = items.filter(name__icontains=item_name)

    paginator = Paginator(items, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obg': page_obj
    }
    return render(request, 'main/catalog.html', context)

@login_required
def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES['upload']
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
        return redirect('/catalog/')
    return render(request, 'main/add-item.html')

@login_required
def update_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.description = request.POST.get('description')
        item.image = request.FILES.get('upload', item.image)
        item.save()
        return redirect('/catalog/')
    context = {
        'item': item
    }
    return render(request, 'main/update-item.html', context)

@login_required
def delete_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == 'POST':
        item.delete()
        return redirect('/catalog/')
    context = {
        'item': item
    }
    return render(request, 'main/delete-item.html', context)

def order(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        products = request.POST.get('products')
        description = request.POST.get('description')
        ord = Order(user=user, products=products, description=description)
        ord.save()
        return redirect('/catalog/')
    return render(request, 'main/order.html')

@login_required
def order_list(request):
    orders = Order.objects.all()
    context = {'orders':orders}
    return render(request, 'main/order-list.html', context)

@login_required
def order_detail(request, my_id):
    ord = Order.objects.get(id=my_id)
    context = {
        'ord':ord
    }
    return render(request, 'main/order-detail.html', context)
