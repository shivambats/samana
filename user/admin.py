from django.contrib import admin
from .models import Address, City, State

# Register your models here.

admin.site.register(Address)
admin.site.register(City)
admin.site.register(State)
