import uuid
from django.db import models
from django.contrib.auth.models import User

class ProductManager(models.Manager):
    def in_stock(self):
        return self.get_queryset().filter(stock__gt=0)
    def sort_decay(self):
        return self.get_queryset().order_by('-price')
    def sort_increasing(self):
        return self.get_queryset().order_by('price')
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    attributes = models.ManyToManyField('Attribute')

    objects = ProductManager()

    class Meta:
        db_table = 'product'
        indexes = [models.Index(fields=['title'])]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    image = models.ImageField(upload_to="products/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name = 'Картинка'
    #     verbose_name_plural = 'Картинки'

class Attribute(models.Model):
    name = models.CharField(max_length=255)

    # class Meta:
    #     verbose_name = 'Атрибут'
    #     verbose_name_plural = 'Атрибуты'

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quntity = models.IntegerField(default=1)