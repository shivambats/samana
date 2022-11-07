from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    parentCategoryId = models.ForeignKey('self', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Attribute(models.Model):
    id = models.SmallAutoField(primary_key=True)
    attribute = models.CharField(max_length=20)

    def __str__(self):
        return self.attribute


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    shortDescription = models.TextField(max_length=500)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    maxPrice = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.brand) + ' ' + str(self.title)


class Variant(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    shortDescription = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    maxPrice = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)
    option = models.CharField(max_length=40)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=
                                    ['product',
                                     'attribute',
                                     'option'],
                                    name='variant_attribute_unique',
                                    ),
        ]

    def __str__(self):
        return str(self.product) + ' ' + str(self.attribute) + ' ' + str(self.option)
