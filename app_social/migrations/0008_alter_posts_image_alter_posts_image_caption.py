# Generated by Django 5.0.6 on 2024-06-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0007_alter_posts_image_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image_caption',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]