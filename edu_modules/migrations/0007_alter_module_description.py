# Generated by Django 4.2.4 on 2023-09-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_modules', '0006_module_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(default=1, max_length=15000, verbose_name='описание'),
            preserve_default=False,
        ),
    ]