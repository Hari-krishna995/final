# Generated by Django 5.0.2 on 2024-04-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_remove_doctor_name_doctor_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
