import uuid

from django.db import models

from user.models import Address
from utils.model_utils import get_uuid
from django.contrib.auth.models import User

# Create your models here.


def get_order_id():
    return get_uuid()


def get_order_item_id():
    return get_uuid()


PAYMENT_MODE = [
    ('CA', 'Cash'),
    ('CR', 'Credit Card'),
    ('GP', 'Google Pay'),
]

ORDER_ITEM_STATUS_CX = [
    ('PLACED', 'PLACED'),
    ('CONFIRMED', 'CONFIRMED'),
    ('SHIPPED', 'SHIPPED'),
    ('OUT FOR DELIVERY', 'OUT FOR DELIVERY'),
    ('DELIVERED', 'DELIVERED'),
    ('RETURN PLACED', 'RETURN PLACED'),
    ('RETURN PROCESSING', 'RETURN PROCESSING'),
    ('RETURN SUCCESSFUL', 'RETURN SUCCESSFUL'),
]


ORDER_STATUS_CX = [
    ('PLACED', 'PLACED'),
    ('CONFIRMED', 'CONFIRMED'),
    ('SHIPPED', 'SHIPPED'),
    ('OUT FOR DELIVERY', 'OUT FOR DELIVERY'),
    ('DELIVERED', 'DELIVERED'),
]


class Order(models.Model):
    id = models.UUIDField(unique=True, default=get_order_id, primary_key=True)
    amount = models.FloatField()
    paymentMode = models.CharField(max_length=2, choices=PAYMENT_MODE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CX, default='PLACED')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return 'OD' + str(self.id)


class OrderItem(models.Model):
    id = models.UUIDField(unique=True, default=get_order_item_id, primary_key=True)
    variant = models.ForeignKey('product.variant', on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, choices=ORDER_ITEM_STATUS_CX)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'OID' + str(self.id)
