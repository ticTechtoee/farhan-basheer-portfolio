# Generated by Django 4.2.7 on 2023-11-27 06:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_contactus_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
