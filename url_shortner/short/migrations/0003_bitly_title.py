# Generated by Django 2.2.2 on 2019-07-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0002_auto_20190701_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitly',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
