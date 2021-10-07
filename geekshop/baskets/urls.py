from django.urls import path
from .views import basket_add,basket_remove

app_name = 'baskets'
urlpatterns = [
    path('add/<int:product_id>/',basket_add,name='basket'),
    path('remove/<int:product_id>/',basket_remove,name='basket_remove')



]


