# Generated by Django 5.0.1 on 2024-01-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_deleted',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]