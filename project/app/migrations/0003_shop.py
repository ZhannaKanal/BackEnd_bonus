# Generated by Django 4.0.4 on 2022-04-28 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_price1_price2_price3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True)),
            ],
        ),
    ]
