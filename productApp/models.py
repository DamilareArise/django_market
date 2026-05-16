from django.db import models

# Create your models here.
# ORM -> object relational mapping
# relationships - one-to-one, one-to-many, many-to-many


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = [
        ("IN_STOCK", 'In Stock'),
        ("OUT_OF_STOCK", 'Out Of Stock'),
    ]
    
    
    title =  models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default="IN_STOCK")
    image = models.ImageField(upload_to="product_images/",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title



  
# categorytable
# cat - A 
# cat - B
  
# producttable
# prod-A   -> cat-A, cat-b
# prod-B  -> cat -A

# productCategory
# prod-A -> cat-a
# prod-A -> cat-b


