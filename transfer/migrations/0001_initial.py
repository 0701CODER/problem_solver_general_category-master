# Generated by Django 4.0.2 on 2022-02-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=65)),
                ('buyer', models.CharField(max_length=65)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
