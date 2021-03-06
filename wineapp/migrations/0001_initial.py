# Generated by Django 2.1.7 on 2019-02-17 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('country', models.TextField()),
                ('description', models.TextField()),
                ('designaion', models.TextField()),
                ('points', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('province', models.TextField()),
                ('region_1', models.TextField(null=True)),
                ('region_2', models.TextField(null=True)),
                ('variety', models.TextField()),
                ('winery', models.TextField()),
            ],
        ),
    ]
