# Generated by Django 3.1.3 on 2020-11-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20201121_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emplyee_regNo', models.TextField(unique=True)),
                ('emplyee_name', models.TextField()),
                ('employee_email', models.TextField()),
                ('employee_mobile', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
