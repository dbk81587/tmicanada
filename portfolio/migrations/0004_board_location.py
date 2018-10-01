# Generated by Django 2.1 on 2018-08-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20180828_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='location',
            field=models.CharField(blank=True, choices=[('Canada', 'Canada'), ('Manitoba', 'Manitoba'), ('British Columbia', 'British Columbia'), ('Alberta', 'Alberta')], default='Canada', help_text='Location', max_length=1),
        ),
    ]