# Generated by Django 2.2.7 on 2019-11-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('taskdesc', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('assingees', models.CharField(max_length=50)),
                ('completed', models.BooleanField(default=False)),
                ('completedby', models.CharField(max_length=50)),
                ('comments', models.CharField(max_length=100)),
            ],
        ),
    ]
