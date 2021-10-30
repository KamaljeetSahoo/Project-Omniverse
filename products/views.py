from django.shortcuts import render
from .models import Brand, Product, ProductImage

# Create your views here.
def landing_page(request):
    return render(request, 'layouts/base1.html')

def product_page(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'pages/products.html', context=context)

def single_product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'pages/single_product_view.html', context=context)

def add_product_view(request):
    return render(request, 'pages/add_product.html')

def handle_add_product(request):
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