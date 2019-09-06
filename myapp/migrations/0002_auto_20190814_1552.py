# Generated by Django 2.2.4 on 2019-08-14 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='instrument',
            field=models.CharField(default='Guitar', max_length=100),
        ),
        migrations.AlterField(
            model_name='musician',
            name='first_name',
            field=models.CharField(help_text='First Name', max_length=100),
        ),
    ]
