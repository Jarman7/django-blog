# Generated by Django 3.0.6 on 2020-05-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200518_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AlterField(
            model_name='about',
            name='github',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='about',
            name='instagram',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='linkedin',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo_link',
            field=models.URLField(),
        ),
    ]
