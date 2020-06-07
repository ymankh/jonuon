from django.contrib import admin
from .models import Material

class Matirials(admin.ModelAdmin):
    pass
admin.site.register(Material, Matirials)