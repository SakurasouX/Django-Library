# Generated by Django 4.0.3 on 2022-04-16 13:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0021_alter_book_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='favorites',
            field=models.ManyToManyField(blank=True, help_text='Choose favorite books', related_name='created', to=settings.AUTH_USER_MODEL),
        ),
    ]
