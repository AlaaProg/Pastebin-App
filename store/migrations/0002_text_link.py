# Generated by Django 3.2.8 on 2021-10-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
