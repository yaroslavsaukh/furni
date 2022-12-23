from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('about/', AboutPage.as_view(), name='about'),
    path('services/', ServicePage.as_view(), name='services'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('contact/', ContactPage.as_view(), name='contact')
]