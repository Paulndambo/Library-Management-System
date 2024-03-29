# Generated by Django 5.0 on 2024-01-24 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0005_remove_book_available_books_book_available"),
        ("users", "0005_member_county"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookissue",
            name="member",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="memberissuedbooks",
                to="users.member",
            ),
        ),
    ]
