# Generated by Django 3.2.5 on 2021-07-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('wallet_id', models.IntegerField()),
            ],
        ),
    ]
