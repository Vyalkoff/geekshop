from django.conf import settings
from django.db import models

# Create your models here.
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from baskets.models import Basket
from products.models import Product


class Order(models.Model):

    FORMING ='FM'
    SEND_TO_PROCEED = 'STP'
    PAID = 'PD'
    PROCEEDED = 'PRD'
    READY ='RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING,'формируется'),
        (SEND_TO_PROCEED,'отпарвленно в обработку'),
        (PAID,'Оплачено'),
        (PROCEEDED,'обрабатывается'),
        (READY,'готов к выдачи'),
        (CANCEL,'отмена заказа'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Создан',auto_now_add=True)
    update = models.DateTimeField(verbose_name='Обновлен',auto_now= True)
    status = models.CharField(choices=ORDER_STATUS_CHOICES,verbose_name='Статус',max_length=3,default= FORMING)
    is_active = models.BooleanField(verbose_name='активен', default=True)


    def __str__(self):
        return f'Текущий заказ {self.pk}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity,items)))

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.get_product_cost(),items)))

    def get_items(self):
        pass

    def delete(self, using=None, keep_parents=False):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.save()
        self.is_active = False
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order,verbose_name='заказ',related_name='orderitems',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name='продукты', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='колличество',default=0)


    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.get(pk=pk).quantity

@receiver(pre_delete,sender = Basket)
@receiver(pre_delete,sender = OrderItem)
def product_quantity_update_delete(sender,instance,**kwargs):
       instance.product.quantity += instance.quantity
       instance.save()


@receiver(pre_save,sender = Basket)
@receiver(pre_save,sender = OrderItem)
def product_quantity_update_delete(sender,instance,**kwargs):
        if instance.pk:
            instance.product.quantity -= instance.quantity - instance.get_item(int(instance.pk))
        else:
            instance.product.quantity -= instance.quantity
        instance.product.save()
