from django.urls import path

# tämän kansion sisällä = .
# sieltä views
# ja import landingview
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct

# path: jos tullaan sovelluksen juureen
# renderöidään landingview
urlpatterns = [
    path('', landingview),
    # Products url's
    path('products/', productlistview),
    path('add-product/', addproduct),
    # Supplier url's
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    
]
