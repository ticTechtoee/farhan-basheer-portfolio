# Generated by Django 3.2.11 on 2022-10-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20221031_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image_1',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image_2',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image_3',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
