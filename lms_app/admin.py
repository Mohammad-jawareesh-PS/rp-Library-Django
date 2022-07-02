from django.contrib import admin
from .models import *
admin.site.register(Book)
admin.site.register(Category)
admin.site.site_header='نظام اداره المكاتب '
admin.site.site_title='نظام اداره المكاتب '

# Register your models here.
