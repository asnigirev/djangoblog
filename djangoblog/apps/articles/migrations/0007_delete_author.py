# Generated by Django 3.0.6 on 2020-05-20 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_remove_article_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
