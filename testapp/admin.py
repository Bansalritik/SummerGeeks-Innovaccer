from django.contrib import admin
from .models import data
# Register your models here.
# Model is registered to be accessed via SuperUser
admin.site.register(data)