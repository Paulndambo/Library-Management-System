# Generated by Django 5.0 on 2024-01-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0002_book_quantity_alter_book_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="rented_out",
            field=models.IntegerField(default=0),
        ),
    ]
