# Generated by Django 2.1.8 on 2019-07-27 01:56

from django.conf import settings
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('strength', 'Strength'), ('cardio', 'Cardio')], db_index=True, default='strength', max_length=250)),
                ('difficulty_level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], db_index=True, default='beginner', max_length=250)),
                ('is_public', models.BooleanField(default=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Weight',
            },
        ),
    ]
