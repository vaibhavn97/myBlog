# Generated by Django 4.1.7 on 2023-03-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='./profile_pics/default.png', upload_to='./profile_pics'),
        ),
    ]
