# Generated by Django 4.2 on 2023-04-17 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pdf_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
