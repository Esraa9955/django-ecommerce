# Generated by Django 4.2.9 on 2024-02-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catgories', '0002_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]