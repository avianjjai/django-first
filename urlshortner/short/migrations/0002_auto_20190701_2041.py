# Generated by Django 2.2.2 on 2019-07-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitly',
            name='email',
        ),
        migrations.AddField(
            model_name='bitly',
            name='username',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
