from django.contrib import admin

# Register your models here.

# jos rekisteröi tälla tavalla adminille oman appin modelit,
# voi myös admin-sivuilta muokata näitä tietoja

from app.models import Supplier, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass
