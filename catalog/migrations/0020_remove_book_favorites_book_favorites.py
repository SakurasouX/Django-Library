# Generated by Django 4.0.3 on 2022-04-14 18:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0019_remove_book_favorites_book_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='favorites',
        ),
        migrations.AddField(
            model_name='book',
            name='favorites',
            field=models.ManyToManyField(help_text='Choose favorite books', related_name='created', to=settings.AUTH_USER_MODEL),
        ),
    ]
