# Generated by Django 4.2.11 on 2024-03-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker_1_db', '0002_alter_books_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_id',
            field=models.CharField(max_length=255),
        ),
    ]
