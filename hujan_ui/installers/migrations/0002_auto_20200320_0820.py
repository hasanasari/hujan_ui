# Generated by Django 2.2.10 on 2020-03-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='system_id',
            field=models.CharField(help_text='unique id MAAS', max_length=220),
        ),
    ]