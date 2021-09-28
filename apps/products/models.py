from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product', null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', null=True)
    name = models.CharField(max_length=255)
    body = models.TextField()
    price = models.IntegerField()
    quantity_of_product = models.IntegerField()
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

