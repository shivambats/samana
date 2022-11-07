from django.db import models
from django.contrib.auth.models import User

from utils.model_utils import get_uuid


def get_addressId():
    return get_uuid()


def get_cityId():
    return get_uuid()


def get_stateId():
    return get_uuid()

# Home = 7-9, Office: 9-5


AddressDeliveryType = [
    ('HOME', 'HOME'),
    ('OFFICE', 'OFFICE'),
    ('OTHER', 'OTHER')
]


class State(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=get_stateId)
    name = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=get_cityId)
    name = models.CharField(max_length=32, null=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=get_addressId)
    title = models.CharField(max_length=10)
    addressType = models.CharField(choices=AddressDeliveryType, default='HOME', max_length=10)
    street = models.CharField(max_length=64, null=False)
    pincode = models.IntegerField(null=False)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    userId = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.street) + ' ' + str(self.city) + ' ' + str(self.city.state)
