from django.contrib import admin
from .models import Maison, Client, Reservation

admin.site.register(Maison)
admin.site.register(Client)
admin.site.register(Reservation)
