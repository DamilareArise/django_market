from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, CategoryForm

# Create your views here.

def homeView(request):
    products = Product.objects.all().order_by("?")[:4]
    # products = Product.objects.filter(id=1)
    # products = Product.objects.get(id=1)
    
    # print(products)
    return render(
        request=request, 
        template_name='index.html',
        context={
            "products": products
        }
    )

def aboutView(request):
    return render(request, 'about.html')


def AddProductView(request):
    if request.method == "POST":
        
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        return redirect("home")
    
    else:
        form = ProductForm()
        return render(
            request=request,
            template_name="product_form.html",
            context={
                "form": form
            }
        )
        
def AddCategoryView(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('add-product')
    
    else:
        form = CategoryForm()
        return render(
            request=request,
            template_name="category_form.html",
            context={
                "form": form
            }
        )
        
def AllProductView(request):
    products = Product.objects.all().order_by("-created_at")
    
    return render(
        request=request,
        template_name="shop.html",
        context={
            "products": products
        }
    )