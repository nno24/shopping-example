# Generated by Django 3.2 on 2022-02-21 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_product_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]