# Generated by Django 4.2.4 on 2023-09-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_modules', '0004_alter_module_description_alter_module_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, max_length=15000, null=True, verbose_name='описание'),
        ),
    ]
