# Generated by Django 2.1.7 on 2019-02-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='description',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]