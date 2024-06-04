# Generated by Django 5.0.6 on 2024-06-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0003_reactioncategory_reaction_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_image',
        ),
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='posts',
            name='image_caption',
            field=models.TextField(default=None),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]