from django.urls import path
from main.views import home, indexItems, about_us, catalog, add_item, update_item, delete_item, order, order_list, order_detail

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about-us'),
    path('catalog/', catalog, name='catalog'),
    path('add-item/', add_item, name='add-item'),
    path('update-item/<int:my_id>/', update_item, name='update-item'),
    path('delete-item/<int:my_id>/', delete_item, name='delete-item'),
    path('catalog/<int:my_id>/', indexItems, name='detail'),
    path('order/', order, name='order'),
    path('order-list/', order_list, name='order-list'),
    path('order-list/<int:my_id>/', order_detail, name='order-detail'),
]