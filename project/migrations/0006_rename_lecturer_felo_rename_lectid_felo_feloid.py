# Generated by Django 4.1.4 on 2023-02-27 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_lecturer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lecturer',
            new_name='Felo',
        ),
        migrations.RenameField(
            model_name='felo',
            old_name='lectid',
            new_name='feloid',
        ),
    ]