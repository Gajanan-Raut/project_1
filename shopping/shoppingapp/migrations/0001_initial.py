# Generated by Django 5.0.1 on 2024-01-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('datails', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('is_deleted', models.CharField(max_length=10)),
            ],
        ),
    ]
