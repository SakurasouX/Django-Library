# Generated by Django 4.0.3 on 2022-04-11 20:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='book_image'),
            preserve_default=False,
        ),
    ]
