# Generated by Django 5.0.4 on 2024-05-23 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('aadhar', models.CharField(default=None, max_length=12)),
                ('address', models.CharField(max_length=255)),
                ('parentname1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('category', models.IntegerField(choices=[(1, 'General'), (2, 'OBC'), (3, 'SC'), (4, 'ST'), (5, 'PwD')])),
            ],
        ),
        migrations.CreateModel(
            name='rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('dob', models.DateField()),
                ('total_12th', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('physics', models.IntegerField()),
                ('chemistry', models.IntegerField(blank=True, default=None, null=True)),
                ('cutoff', models.FloatField()),
                ('Rank', models.IntegerField(blank=True, null=True)),
                ('random_no', models.CharField(blank=True, max_length=5, null=True, unique=True)),
            ],
        ),
    ]