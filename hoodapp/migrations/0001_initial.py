# Generated by Django 2.2 on 2020-11-01 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('description', tinymce.models.HTMLField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('notification', tinymce.models.HTMLField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
            ],
        ),
    ]
