# Generated by Django 5.1.4 on 2024-12-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_received', models.DateField()),
                ('received_by', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
