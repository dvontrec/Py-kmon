# Generated by Django 2.2 on 2019-04-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_name', models.CharField(max_length=255)),
                ('pokemon_type', models.CharField(max_length=255)),
                ('pokemon_number', models.CharField(max_length=3)),
            ],
        ),
    ]