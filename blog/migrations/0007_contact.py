# Generated by Django 3.0.6 on 2020-05-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200517_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('instagram', models.URLField()),
            ],
        ),
    ]
