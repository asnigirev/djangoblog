# Generated by Django 3.0.6 on 2020-05-20 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200520_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default='Noname', on_delete=django.db.models.deletion.CASCADE, to='articles.Author'),
        ),
    ]