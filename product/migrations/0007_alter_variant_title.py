# Generated by Django 4.0.3 on 2022-04-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_attribute_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
