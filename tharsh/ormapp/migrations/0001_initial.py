# Generated by Django 5.1.7 on 2025-04-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(help_text='User ID', max_length=20)),
                ('user_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('movie_name', models.CharField(max_length=200)),
                ('show_datetime', models.DateTimeField()),
                ('no_of_seats', models.IntegerField()),
            ],
        ),
    ]
