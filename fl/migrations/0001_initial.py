# Generated by Django 4.2.11 on 2024-05-05 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sku', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('Size', models.CharField(max_length=50)),
                ('Weight', models.CharField(max_length=50)),
                ('Capacity', models.CharField(max_length=50)),
                ('Material', models.CharField(max_length=100)),
                ('Non_slip_legs', models.CharField(max_length=5)),
                ('category', models.CharField(max_length=100)),
                ('LastScrappeddate', models.DateTimeField(auto_now=True)),
                ('Updateddate', models.DateTimeField(auto_now=True)),
                ('Createddate', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(max_length=50)),
                ('main_image_url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_url', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fl.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]
