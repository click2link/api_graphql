from django.contrib import admin
from api_ventas.ventas.models import Venta

class VentaAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Venta._meta.fields]

admin.site.register(Venta, VentaAdmin)
