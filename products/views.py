from django.shortcuts import redirect, render
from .models import Brand, Product, ProductImage

# Create your views here.
def landing_page(request):
    if request.user.is_authenticated:
        return render(request, 'layouts/base1.html')
    else:
        return redirect('login')

def product_page(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'pages/products.html', context=context)
    else:
        return redirect('login')

def single_product_view(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        context = {
            'product': product
        }
        return render(request, 'pages/single_product_view.html', context=context)
    else:
        return redirect('login')

def add_product_view(request):
    if request.user.is_authenticated:
        return render(request, 'pages/add_product.html')
    else:
        return redirect('login')

def handle_add_product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            bnd = request.POST['brand']
            try:
                brand = Brand.objects.get(brand_name = bnd)
            except:
                brand = Brand.objects.get(id=1)
            product = Product(name=request.POST['name'], description=request.POST['description'], price = request.POST['price'], brand=brand)
            product.save()
            images = request.FILES.getlist('images')
            for image in images:
                img = ProductImage(image=image)
                img.save()
                product.image.add(img)
                product.save()
            return render(request, 'pages/add_product.html')
        else:
            return render(request, 'pages/add_product.html')
    else:
        return redirect('login')