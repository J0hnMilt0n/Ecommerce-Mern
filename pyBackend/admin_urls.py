from django.urls import path
from users.views import admin_login
from products.views import create_product, update_product, delete_product, bulk_import_products
from orders.views import get_all_orders, get_admin_order_by_id, update_order_status, add_admin_note, get_dashboard_stats, export_orders_csv

urlpatterns = [
    # Auth
    path('auth/login', admin_login, name='admin_login'),
    
    # Products
    path('products', create_product, name='admin_create_product'),
    path('products/<int:pk>', update_product, name='admin_update_product'),
    path('products/<int:pk>/delete', delete_product, name='admin_delete_product'),
    path('products/import', bulk_import_products, name='bulk_import_products'),
    
    # Orders
    path('orders', get_all_orders, name='admin_get_all_orders'),
    path('orders/<int:pk>', get_admin_order_by_id, name='admin_get_order_by_id'),
    path('orders/<int:pk>/status', update_order_status, name='update_order_status'),
    path('orders/<int:pk>/notes', add_admin_note, name='add_admin_note'),
    path('orders/export', export_orders_csv, name='export_orders_csv'),
    path('orders/dashboard/stats', get_dashboard_stats, name='dashboard_stats'),
]
