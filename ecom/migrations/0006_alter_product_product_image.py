# Generated by Django 4.2 on 2024-12-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]
