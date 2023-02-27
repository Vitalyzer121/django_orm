# Generated by Django 4.1.5 on 2023-02-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0011_remove_movie_director_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director_email',
            field=models.EmailField(default='sugar_daddy@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Квентин Тарантино', max_length=100),
        ),
    ]