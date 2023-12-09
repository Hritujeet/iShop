from django.shortcuts import HttpResponse, render, redirect
from .models import Product, Review
from user.models import Cart, Order
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        allProducts = []

        catProducts = Product.objects.values('category', 'id')
        categories = {item['category'] for item in catProducts}
        for category in categories:
            prod = Product.objects.filter(category=category)
            allProducts.append([prod, range(0, len(prod)), len(prod)])
        params = {'allProducts':allProducts}
        return render(request, 'shop/shopHome.html', params)


def about(request):
    return render(request, 'shop/about.html')


def orders(request):
    orderItems = Order.objects.filter(user=request.user)

    params = {"orders":orderItems}
    return render(request, 'user/orders.html', params)


def productView(request , slug):
    product = Product.objects.filter(name=slug).first()
    print(product.name)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        content = request.POST.get('content')

        if(int(rating)>5):
            messages.add_message(request, messages.ERROR, "Ratings Should be out of 5")
        else:
            newReview = Review(rating=rating, user=request.user, product=product, content=content)
            newReview.save()
            messages.add_message(request, messages.SUCCESS, "Review has been posted successfully")
        return redirect(f"/products/productView/{product.name}")
    reviews = Review.objects.filter(product=product)

    params = {"product":product, "reviews":reviews}
    return render(request, 'shop/productView.html', params)

def myCart(request):
    userItems = Cart.objects.filter(user=request.user)
    print(userItems)

    params = {'cartItems':userItems}
    return render(request,"shop/myCart.html", params)

def addToCart(request):
    if request.method == 'POST':
        itemId = request.POST.get("item")
        userName = request.POST.get("user")

        item = Product.objects.filter(id=itemId).first()
        user = User.objects.filter(username=userName).first()
        
        cartItem = Cart(user=user, item=item)
        cartItem.save()
        messages.add_message(request, messages.SUCCESS, "Item Added To Cart Successfully")

        return redirect('myCart')
    else:
        return HttpResponse("403 - Forbidden")


def tracker(request):
    return HttpResponse("This is Tracker")


def removeCart(request):
    if request.method == 'POST':
        itemId = request.POST.get("delItem")
        userName = request.POST.get("delUser")

        item = Product.objects.filter(id=itemId).first()
        user = User.objects.filter(username=userName).first()

        i = Cart.objects.filter(item=item).first()

        i.delete()
        messages.add_message(request, messages.SUCCESS, "Item has been removed from your Cart")

        return redirect('myCart')
    else:
        return HttpResponse("403 - Forbidden")


def checkout(request):
    userItems = Cart.objects.filter(user=request.user)
    # Calculating Total Amount
    sum = 0
    for item in userItems:
        sum += item.item.price
    
    if request.method == "POST":
        orderItems = []
        address = request.POST.get('addr')
        phNumber = request.POST.get('phone')

        for item in userItems:
            orderItems.append(Order(item=item, user=request.user, address=address, contactNum=phNumber, status="Ordered"))

        for i in orderItems:
            i.save()

        messages.add_message(request, messages.SUCCESS, "Your Order has been placed")

        return redirect('/orders')

    params = {'items':userItems, 'total':sum}
    return render(request, 'shop/checkout.html', params)

def contact(request):
    return render(request,'shop/contact.html')
