# Generated by Django 4.2.7 on 2024-04-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0008_auto_20240325_1259"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description2",
            field=models.TextField(default="Default Description"),
        ),
        migrations.AddField(
            model_name="product",
            name="image2",
            field=models.ImageField(
                default="products/default.jpg", upload_to="products/"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="image3",
            field=models.ImageField(
                default="products/default.jpg", upload_to="products/"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="image4",
            field=models.ImageField(
                default="products/default.jpg", upload_to="products/"
            ),
        ),
    ]
