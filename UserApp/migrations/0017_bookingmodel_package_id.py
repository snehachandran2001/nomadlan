# Generated by Django 4.2.9 on 2024-04-16 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AgentApp', '0015_hotelmodel_hotel_description'),
        ('UserApp', '0016_remove_bookingmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='package_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AgentApp.packagemodel'),
        ),
    ]