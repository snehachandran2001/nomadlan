# Generated by Django 4.2.9 on 2024-04-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgentApp', '0011_alter_packageimagesmodel_package_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagemodel',
            name='is_recommended',
            field=models.BooleanField(default=False),
        ),
    ]
