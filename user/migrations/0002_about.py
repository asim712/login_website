# Generated by Django 4.0.2 on 2022-02-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=50)),
                ('high_title', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
        ),
    ]