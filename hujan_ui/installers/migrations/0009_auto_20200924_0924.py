# Generated by Django 2.2.10 on 2020-09-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installers', '0008_installer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='description',
            field=models.CharField(blank=True, max_length=220),
        ),
    ]
