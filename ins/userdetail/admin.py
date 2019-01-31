from django.contrib import admin

# Register your models here.
from .models import Vehicle, User

admin.site.register(Vehicle)
admin.site.register(User)