# Generated by Django 3.2.4 on 2021-06-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject', '0003_remove_inquiry_query_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='result',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
