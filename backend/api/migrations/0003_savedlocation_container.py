# Generated by Django 4.1.7 on 2023-03-12 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_savedlocation_savedlocations'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedlocation',
            name='container',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.savedlocations'),
            preserve_default=False,
        ),
    ]
