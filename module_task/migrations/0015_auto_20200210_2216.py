# Generated by Django 3.0.2 on 2020-02-10 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_task', '0014_auto_20200210_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='assingees',
            field=models.ForeignKey(blank=True, default='staff member deleted', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='module_task.StaffList'),
        ),
    ]
