# Generated by Django 5.0.3 on 2024-04-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_messperiod_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
