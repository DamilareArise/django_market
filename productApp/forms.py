from django import forms
from .models import Product, ProductCategory



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "quantity",
            "price",
            "category",
            "image"
        ]
        
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True)
    class Meta:
        model = ProductCategory
        fields = [
            "name",
            "description"
        ]
        