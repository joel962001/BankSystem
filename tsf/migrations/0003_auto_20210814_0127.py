# Generated by Django 3.1.7 on 2021-08-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsf', '0002_auto_20210814_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='acc',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
