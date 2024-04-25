# Generated by Django 4.2.9 on 2024-03-06 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AgentApp', '0001_initial'),
        ('UserApp', '0002_alter_booking_ser_adult_alter_booking_ser_children'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('num_adult', models.IntegerField()),
                ('num_children', models.IntegerField()),
                ('special_request', models.CharField(max_length=255)),
                ('payment_status', models.CharField(max_length=255)),
                ('status', models.CharField(default='Pending', max_length=255)),
                ('package_hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgentApp.packagehotel')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_type', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'payment_type',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=255)),
                ('user_password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Active', max_length=255)),
            ],
            options={
                'db_table': 'user_data',
            },
        ),
        migrations.RemoveField(
            model_name='booking_ser',
            name='adult',
        ),
        migrations.RemoveField(
            model_name='booking_ser',
            name='children',
        ),
        migrations.RemoveField(
            model_name='booking_ser',
            name='return1',
        ),
        migrations.AlterModelTable(
            name='booking_ser',
            table=None,
        ),
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('payment_status', models.CharField(max_length=255)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.bookingmodel')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.paymenttype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1)),
                ('review', models.TextField(max_length=500)),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgentApp.packagemodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel'),
        ),
    ]
