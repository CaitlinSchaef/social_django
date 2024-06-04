# Generated by Django 5.0.6 on 2024-06-04 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReactionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, null=True)),
                ('comment_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_social.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post_body', models.CharField(max_length=2000, null=True)),
                ('comments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_social.comment')),
                ('post_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_social.profile')),
                ('post_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_social.postcategory')),
                ('post_image', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_social.image')),
                ('reactions', models.ManyToManyField(default=None, to='app_social.reactioncategory')),
            ],
        ),
    ]
