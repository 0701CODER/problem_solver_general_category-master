# Generated by Django 4.0.2 on 2022-02-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='code',
            field=models.CharField(default='7890', max_length=65),
        ),
    ]
