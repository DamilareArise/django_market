from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, CategoryForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .utils import is_staff_user
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

# @login_required()
@user_passes_test(is_staff_user)
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
        
@user_passes_test(is_staff_user)        
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
    
def GetProductView(request, id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)
    return render(
        request=request,
        template_name="single_product.html",
        context={
            "product":product
        }
    )

@user_passes_test(is_staff_user)
def DeleteProductView(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    
    return redirect("shop")


@user_passes_test(is_staff_user)
def EditProductView(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            
        return redirect("shop")
    
    else:
        form = ProductForm(instance=product)
        return render(
            request=request,
            template_name="edit_product_form.html",
            context={
                "form": form
            }
        )