# Generated by Django 4.2.9 on 2024-02-04 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options_product_category_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updateat',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
