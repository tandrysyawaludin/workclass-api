# Generated by Django 3.1.5 on 2021-01-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=1000)),
                ('job_title', models.CharField(max_length=1000)),
                ('logo_url', models.CharField(max_length=1000)),
                ('date', models.DateField()),
            ],
        ),
    ]
