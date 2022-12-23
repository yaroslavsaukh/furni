from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, TemplateView
from .models import *


# Create your views here.


class HomePage(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_items'] = Furniture.objects.all()[:3]
        context['services'] = Services.objects.all()[:4]
        context['popular_furniture'] = Furniture.objects.order_by('?')[:3]
        context['testimonials'] = Testimonial.objects.all()
        return context


class ShopPage(ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Furniture.objects.all()


class AboutPage(TemplateView):
    template_name = 'shop/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['services'] = Services.objects.all()[:4]
        context['testimonials'] = Testimonial.objects.all()
        context['team'] = Team.objects.all()
        return context


class ServicePage(TemplateView):
    template_name = 'shop/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Services'
        context['services'] = Services.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['popular_furniture'] = Furniture.objects.order_by('?')[:3]
        return context


class BlogPage(TemplateView):
    template_name = 'shop/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['blog_items'] = BlogItem.objects.all()
        context['testimonials'] = Testimonial.objects.all()

        return context

class ContactPage(TemplateView):
    template_name = 'shop/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact us'
        return context