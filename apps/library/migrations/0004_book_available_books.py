# Generated by Django 5.0 on 2024-01-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0003_book_rented_out"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="available_books",
            field=models.IntegerField(default=0),
        ),
    ]