# Generated by Django 4.2.4 on 2023-12-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProjects', '0011_delete_interessen'),
    ]

    operations = [
        migrations.AddField(
            model_name='projekt',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]