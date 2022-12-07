from django.contrib import admin
from .models import  User, Book, flight

# Register your models here.

admin.site.register(flight)
admin.site.register(User)
admin.site.register(Book)


