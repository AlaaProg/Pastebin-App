# Generated by Django 3.2.8 on 2021-10-28 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_text_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='link',
            new_name='hash',
        ),
    ]
