# Generated by Django 5.0.1 on 2024-02-15 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pid',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
