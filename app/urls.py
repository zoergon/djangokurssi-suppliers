from django.urls import path

# tämän kansion sisällä = .
# sieltä views
# ja import landingview
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct, \
    deleteproduct, confirmdeleteproduct, edit_product_get, edit_product_post, products_filtered, \
        searchsuppliers

# path: jos tullaan sovelluksen juureen
# renderöidään landingview
urlpatterns = [
    path('', landingview),
    # Products url's
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),

    # Supplier url's
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('search-suppliers/', searchsuppliers),
]
