# Generated by Django 3.2.5 on 2021-07-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
