# Generated by Django 4.2.9 on 2024-02-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_created_alter_product_updateat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.jpg', null=True, upload_to='product_images'),
        ),
    ]