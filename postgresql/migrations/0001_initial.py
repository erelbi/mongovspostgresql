# Generated by Django 3.2.4 on 2021-06-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonPostgresql',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('surname', models.CharField(max_length=20, null=True)),
                ('year', models.IntegerField()),
                ('school', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
