# Generated by Django 4.2.1 on 2023-06-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0011_reports'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('Fid', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('Assets', models.CharField(max_length=100000)),
                ('Number', models.TextField()),
            ],
            options={
                'db_table': 'farm_overview',
            },
        ),
    ]