# Generated by Django 5.1.6 on 2025-02-07 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, upload_to='categories', verbose_name='avatar')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Caregories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, upload_to='products', verbose_name='avatar')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('Category', models.ManyToManyField(blank=True, to='products.category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('file', models.FileField(upload_to='files/%y/%m/%d/', verbose_name='file')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'db_table': 'file',
            },
        ),
    ]
