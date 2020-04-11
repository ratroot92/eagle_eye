# Generated by Django 3.0.5 on 2020-04-06 15:20

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_followersnames'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitter_target',
            name='submission_date',
        ),
        migrations.AddField(
            model_name='twitter_target',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitter_target',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='twitter_target',
            name='target_platform',
            field=models.CharField(default='twitter', max_length=255, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='twitter_target',
            name='target_scheduling',
            field=models.CharField(choices=[('', 'Select Target Scheuling'), ('1hr', 'Every One Hour'), ('6hr', 'Every Six Hour'), ('12hr', 'Every Twelve Hour'), ('24hr', 'Every Day ')], max_length=255),
        ),
        migrations.AlterField(
            model_name='twitter_target',
            name='target_type',
            field=models.CharField(default='twitter_person', max_length=255),
        ),
        migrations.AlterField(
            model_name='twitter_target',
            name='twitter_username',
            field=models.CharField(max_length=255),
        ),
    ]