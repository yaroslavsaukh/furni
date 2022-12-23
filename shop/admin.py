from django.contrib import admin
from .models import *

# Register your models here.
from django.utils.safestring import mark_safe


class GetImage:
    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')


class FurnitureAdmin(admin.ModelAdmin, GetImage):
    list_display = ('name', 'price', 'get_img')
    list_display_links = ('name', 'get_img')
    search_fields = ('name',)
    list_filter = ('price',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')

    get_img.short_description = "Photo"


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'get_img')
    list_display_links = ('name',)
    list_filter = ('position',)
    search_fields = ('name',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')

    get_img.short_description = "Photo"


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'get_img')
    list_display_links = ('pk', 'get_img')
    search_fields = ('body',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subscribe_date')
    list_display_links = ('email', 'name')
    list_filter = ('subscribe_date',)
    search_fields = ('name', 'email')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'added_at', 'get_img')
    list_display_links = ('title', 'get_img')
    list_filter = ('added_at',)
    search_fields = ('title',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_img')
    list_display_links = ('title', 'get_img')
    search_fields = ('title',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'coupon', 'f_name', 'l_name')
    list_display_links = ('pk',)
    list_filter = ('coupon', 'country', 'created_at')
    search_fields = ('pk',)
    save_on_top = True


class CouponAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')


admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(EmailSubscribers, EmailAdmin)
admin.site.register(BlogItem, BlogAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon, CouponAdmin)
