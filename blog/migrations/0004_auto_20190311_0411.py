# Generated by Django 2.1.7 on 2019-03-11 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190311_0410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posttranslation',
            old_name='language_code',
            new_name='language',
        ),
    ]