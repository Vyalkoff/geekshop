from django.urls import path
from .views import basket_add, basket_remove, basket_edit

app_name = 'baskets'
urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket'),
    path('remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path('edit/<int:bask_id>/<int:quantity>/', basket_edit, name='basket_edit')

]
