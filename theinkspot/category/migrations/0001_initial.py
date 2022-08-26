# Generated by Django 3.2.12 on 2022-08-03 23:21

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(choices=[('sports', 'Sports'), ('computer science', 'Computer Science'), ('Physics', 'Physics'), ('space', 'Space'), ('cinema', 'Cinema'), ('music', 'Music'), ('economy', 'Economy')], max_length=50, unique=True, verbose_name='Category Name')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
