# Generated by Django 4.2.9 on 2024-02-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='products/images/'),
        ),
    ]