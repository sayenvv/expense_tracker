# Generated by Django 4.0.5 on 2022-06-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_trackerAPP', '0003_remove_cieduser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('suspended', 'suspended')], default='Active', max_length=25)),
            ],
        ),
    ]
