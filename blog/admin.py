from django.contrib import admin
from .models import *


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')


admin.site.register(Blog, BlogAdmin)