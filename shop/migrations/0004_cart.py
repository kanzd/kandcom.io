# Generated by Django 3.0.7 on 2020-06-13 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('payment', models.BooleanField()),
            ],
        ),
    ]