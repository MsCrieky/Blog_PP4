# Generated by Django 4.2.9 on 2024-02-05 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_excerpt_post_updated_on_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
