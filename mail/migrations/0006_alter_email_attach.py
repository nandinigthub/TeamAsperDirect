# Generated by Django 4.1.3 on 2022-12-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0005_remove_email_archived_remove_email_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='attach',
            field=models.FileField(blank='', default='', upload_to='doc'),
        ),
    ]