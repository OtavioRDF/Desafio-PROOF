# Generated by Django 4.1 on 2022-08-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_bannedips_id_alter_ips_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannedips',
            name='bannedIPs',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='ips',
            name='IPs',
            field=models.CharField(max_length=60),
        ),
    ]
