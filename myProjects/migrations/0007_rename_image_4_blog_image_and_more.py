# Generated by Django 4.2.4 on 2023-12-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProjects', '0006_remove_projekt_plot_1_remove_projekt_plot_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image_4',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='projekt',
            old_name='beschreibung',
            new_name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='kurzbeschreibung',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projekt',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='projekt',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='projekt',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='projekt',
            name='kurzbeschreibung',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
    ]
