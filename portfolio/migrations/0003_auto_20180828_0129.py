# Generated by Django 2.1 on 2018-08-28 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_board_memo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ['-id']},
        ),
    ]