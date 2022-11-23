from django.urls import path

# tämän kansion sisällä = .
# sieltä views
# ja import landingview
from .views import landingview, productlistview, supplierlistview

# path: jos tullaan sovelluksen juureen
# renderöidään landingview
urlpatterns = [
    path('', landingview),
    # Products url's
    path('products/', productlistview),
    # Supplier url's
    path('suppliers/', supplierlistview),
    
]
