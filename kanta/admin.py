from django.contrib import admin

from .models import Onnettomuus, SuosittuHaku, Vierailu

admin.register(Onnettomuus, SuosittuHaku, Vierailu)(admin.ModelAdmin)
