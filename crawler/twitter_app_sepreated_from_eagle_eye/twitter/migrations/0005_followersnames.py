# Generated by Django 3.0.5 on 2020-04-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_retweets'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersNames',
            fields=[
                ('user', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('time_update', models.IntegerField()),
                ('follower', models.TextField()),
            ],
        ),
    ]
