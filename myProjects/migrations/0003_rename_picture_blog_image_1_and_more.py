# Generated by Django 4.2.4 on 2023-11-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProjects', '0002_blog_rename_projekt_projekt_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='picture',
            new_name='image_1',
        ),
        migrations.RenameField(
            model_name='projekt',
            old_name='bild',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='projekt',
            old_name='plots',
            new_name='plot_1',
        ),
        migrations.RenameField(
            model_name='projekt',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='blog',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='projekt',
            name='plot_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='projekt',
            name='plot_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='projekt',
            name='plot_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='projekt',
            name='plot_5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
