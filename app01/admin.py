from django.contrib import admin
from app01.models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    model = Blog

admin.site.register(Blog, BlogAdmin)    