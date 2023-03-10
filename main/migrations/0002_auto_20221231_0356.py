# Generated by Django 3.2.13 on 2022-12-31 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.SlugField()),
                ('project_description', models.TextField()),
                ('project_link', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Extracurricular',
        ),
        migrations.DeleteModel(
            name='ObjectiveHead',
        ),
        migrations.DeleteModel(
            name='OtherLink',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
