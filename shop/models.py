import datetime

from django.db import models
from django.utils.timezone import now


# Create your models here.


class Furniture(models.Model):
    image = models.ImageField(upload_to='photos/furniture')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    short_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Furniture Item'
        verbose_name_plural = 'Furniture'


class Team(models.Model):
    image = models.ImageField(upload_to='photos/team')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Team'


class Testimonial(models.Model):
    author = models.ForeignKey('Team', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/testimonials')
    body = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class EmailSubscribers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subscribe_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'


class BlogItem(models.Model):
    image = models.ImageField(upload_to='photos/blog')
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Team', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'BlogItem'
        verbose_name_plural = 'BlogItems'


class Services(models.Model):
    image = models.ImageField(upload_to='photos/services')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=160)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Cart(models.Model):
    products = models.ForeignKey('Furniture', on_delete=models.CASCADE)
    count = models.IntegerField()
    total = models.IntegerField()
    coupon = models.CharField(max_length=4)


class Order(models.Model):
    country = models.CharField(max_length=40)
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    company = models.CharField(max_length=60, blank=True)
    street = models.CharField(max_length=60)
    apartment = models.CharField(max_length=60)
    email = models.EmailField()
    zip = models.IntegerField()
    phone = models.CharField(max_length=12)
    notes = models.TextField()
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    coupon = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class Coupon(models.Model):
    name = models.CharField(max_length=4)

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = "Coupons"
