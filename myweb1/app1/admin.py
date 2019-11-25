from django.contrib import admin

# Register your models here.

from .models import Login #계정, 비번, 이름

admin.site.register(Login)