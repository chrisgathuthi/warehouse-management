
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.




class Stock(models.Model):
    tags =[
        ("cereals", "cereals"),
        ("flour", "flour"),
        ("dairy", "dairy"),
        ("oil", "oil"),
    ]
    storage =[
        ("freezer", "freezer"),
        ("dry", "dry"),
        ("low", "low"),
        ("canned", "canned"),
    ]
    ISLE = [
        ("one",1),
        ("two",2),
        ("three",3),
        ("four",4),
        ("five",5),
    ]
    product_name = models.CharField(verbose_name="product name",max_length=100)
    net_weight = models.PositiveIntegerField(verbose_name="weight in tonnes")
    qty = models.PositiveIntegerField(verbose_name="quantity")
    date = models.DateField(verbose_name="date of stock",auto_created=True,auto_now_add=True)
    isle = models.CharField(verbose_name="shelf no:",max_length=5,choices=ISLE,default=[0][0])
    tags = models.CharField(verbose_name="select tag",max_length=50,choices=tags)
    storage = models.CharField(verbose_name="storage conditions",max_length=50,choices=storage)
    shelf_life = models.DurationField(null=True)
    exp = models.DateField(verbose_name="Expiry date",null=True)
    attendant = models.ForeignKey(to=User,related_name="handler",on_delete = models.CASCADE,verbose_name="handler",default=1)
    status = models.CharField(verbose_name="comment",max_length=25,null=True)
  

    # @property
    # def Url(self):
    #     if self.docs == "":
    #         self.docs= ""
    #     return self.docs

    def __str__(self) -> str:
        return f"{self.product_name}"
    
    @classmethod
    def company(cls):
        return cls.company

    @staticmethod
    def get_date():
        return datetime.today()
    
    class Meta:
        permissions =[
            ("can_allow_dispatch", "can allow dispatch"),
            ("can_make_reorders", "can make new orders"),
        ]
        ordering = ["product_name","-date"]
    
    def get_absolute_url(self):
        return reverse("shop:detail-page",kwargs={"pk":self.pk})

class Sales(models.Model):
    employee = models.ForeignKey(User,on_delete=models.CASCADE,related_name="seller",verbose_name="attendant")
    stock_sold = models.ForeignKey(Stock,on_delete=models.CASCADE,related_name="item",verbose_name="Stock sold")
    stock_qty = models.PositiveIntegerField(verbose_name="quantity sold")
    date = models.DateTimeField(auto_now_add=True)

    

    def __str__(self) -> str:
        return f"{self.stock_sold}"

    class Meta:
        permissions =[
            ("can_allow_dispatch", "can allow dispatch"),
        ]
        ordering = ["-date"]


class Department(models.Model):
    name = models.CharField(verbose_name="name",max_length=10)
    

class Employee(models.Model):
    name = models.CharField(max_length=10)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    


    
