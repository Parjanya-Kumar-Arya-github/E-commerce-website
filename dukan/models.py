from django.db import models
from django.utils import timezone


# Create your models here.
class saman(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    product_desc = models.CharField(max_length=200000, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/", default="")
    category = models.CharField(max_length=50,default='')
    mfd = models.TimeField(default=timezone.now())

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    cont_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20,default="")
    message = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    def __str__(self):
        return self.name
class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."