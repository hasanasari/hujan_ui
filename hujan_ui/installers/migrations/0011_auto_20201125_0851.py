# Generated by Django 2.2.10 on 2020-11-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installers', '0010_auto_20201109_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('success', 'Success'), ('failed', 'Failed'), ('post_in_progress', 'Deploy Kolla'), ('post_success', 'Deploy Success'), ('post_failed', 'Deploy Failed')], max_length=255),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='network_interface',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='storage_interface',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]