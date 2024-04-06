# Generated by Django 4.2.4 on 2023-11-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.CharField(max_length=200, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('theme', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='projekt',
            old_name='projekt',
            new_name='name',
        ),
    ]