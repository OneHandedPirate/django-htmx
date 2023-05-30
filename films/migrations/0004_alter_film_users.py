# Generated by Django 3.2.8 on 2023-05-30 08:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20230530_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='users',
        ),
        migrations.AddField(
          model_name='film',
          name='users',
          field=models.ManyToManyField(related_name='films', through='films.UserFilms', to=settings.AUTH_USER_MODEL),
        ),

    ]
