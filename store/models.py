from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True) # a slug field is part of the request URI path which can act as a service/resource identifier; in this case it can be /<category_name>/.../<product_name>, any special characters entered will be formatted in a URL/URI safe manner

    class Meta:
        verbose_name_plural = 'categories' # django may use plural form of the Model name i.e., Category as Categorys which is wrong, so an additional data which is the plural alternative is provided
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE) # if a category is deleted, then all products linked to that category or belonging to that category are deleted
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/') # upload images to this folder
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True) # is product available to buy even though in stock
    created = models.DateTimeField(auto_now_add=True) # fills in the timestamp value when the entry is created
    updated = models.DateTimeField(auto_now=True) # updates the field when the entry is updated

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',) # when the data is returned it sorts by the created timestamp in desc order
        # ordering = ('created',) # when the data is returned it sorts by the created timestamp in asc order

    def __str__(self) -> str:
        return self.title