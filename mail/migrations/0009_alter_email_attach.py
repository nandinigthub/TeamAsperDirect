# Generated by Django 4.1.3 on 2022-12-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0008_alter_email_attach_alter_email_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='attach',
            field=models.FileField(blank='', default='', upload_to='doc'),
        ),
    ]
