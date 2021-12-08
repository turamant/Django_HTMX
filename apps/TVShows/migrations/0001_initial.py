# Generated by Django 4.0 on 2021-12-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EightiesKidsTVShows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('decade', models.IntegerField(default=1980)),
                ('blurb', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]
