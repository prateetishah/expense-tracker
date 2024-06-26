# Generated by Django 4.2.11 on 2024-03-24 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.PositiveBigIntegerField(unique=True)),
                ('title', models.CharField(max_length=1000)),
                ('subtitle', models.CharField(max_length=1000, null=True)),
                ('authors', models.CharField(max_length=1000)),
                ('publisher', models.CharField(max_length=1000)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('category', models.CharField(max_length=1000)),
                ('distribution_expense', models.FloatField(default='', null=True)),
            ],
        ),
    ]
