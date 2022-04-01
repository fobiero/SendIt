from django.contrib import admin
from .models import Customer, Sender, newdestination
# Register your models here.

admin.site.register(Customer)
admin.site.register(Sender)
admin.site.register(newdestination)
