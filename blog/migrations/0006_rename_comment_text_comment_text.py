# Generated by Django 4.2 on 2023-07-01 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_publish_post_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_text',
            new_name='text',
        ),
    ]
