# Generated by Django 4.2.4 on 2023-11-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projekt', models.CharField(max_length=200, null=True)),
                ('beschreibung', models.TextField(blank=True, null=True)),
                ('bild', models.ImageField(blank=True, null=True, upload_to='')),
                ('plots', models.ImageField(blank=True, null=True, upload_to='')),
                ('skills', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]