# Generated by Django 2.2.7 on 2019-11-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0016_question_youtube_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Option'),
        ),
    ]
