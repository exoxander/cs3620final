# Generated by Django 4.2.3 on 2023-08-14 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileimage', models.ImageField(default='NotFound.jpg', upload_to='profileimages')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postname', models.CharField(max_length=20)),
                ('postdescription', models.CharField(max_length=2048)),
                ('postimage', models.ImageField(default='NotFound.jpg', upload_to='postimages')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.profile')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentdata', models.CharField(max_length=128)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
