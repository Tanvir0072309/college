# Generated by Django 5.1.4 on 2025-01-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_admissionform_form_no_alter_class_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionform',
            name='aadhar',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='admissionform',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
