# Generated by Django 4.2.4 on 2023-12-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProjects', '0008_projekt_github_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AddField(
            model_name='projekt',
            name='structure',
            field=models.TextField(blank=True, null=True),
        ),
    ]
