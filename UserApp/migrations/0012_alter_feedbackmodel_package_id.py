# Generated by Django 4.2.9 on 2024-04-07 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AgentApp', '0012_packagemodel_is_recommended'),
        ('UserApp', '0011_alter_wishlistmodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='package_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgentApp.packagemodel'),
        ),
    ]