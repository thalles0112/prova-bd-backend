# Generated by Django 5.1 on 2024-08-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_venda_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='whatsapp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
