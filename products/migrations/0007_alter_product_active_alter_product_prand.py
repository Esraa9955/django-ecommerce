# Generated by Django 4.2.9 on 2024-02-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='prand',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]