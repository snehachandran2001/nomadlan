# Generated by Django 4.2.9 on 2024-04-02 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AgentApp', '0007_offermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offermodel',
            name='applicable_packages',
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='AgentApp.offermodel'),
        ),
    ]