# Generated by Django 3.2.3 on 2022-01-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stegnography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decoding',
            name='files',
            field=models.FileField(upload_to='documents/decoding/'),
        ),
        migrations.AlterField(
            model_name='decoding',
            name='types',
            field=models.CharField(blank=True, choices=[('midi', 'MIDI'), ('wave', 'WAVE')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='types',
            field=models.CharField(blank=True, choices=[('midi', 'MIDI'), ('wave', 'WAVE')], default=False, max_length=20),
        ),
    ]
