# Generated by Django 4.2.7 on 2023-12-02 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role_productimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImage',
            new_name='UserImage',
        ),
    ]
