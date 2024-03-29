# Generated by Django 4.0.2 on 2022-02-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_rename_upload_view_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='new_owner',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='upload',
            name='new_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='upload',
            name='previous_owner',
            field=models.CharField(default=models.IntegerField(), max_length=64),
        ),
    ]
