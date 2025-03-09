# Generated by Django 5.1.4 on 2025-01-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_alter_admissionform_aadhar_alter_admissionform_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='faculty/photos/')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=100)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('education', models.CharField(max_length=255)),
                ('function', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('research', models.TextField()),
                ('publications_national', models.PositiveIntegerField(default=0)),
                ('publications_international', models.PositiveIntegerField(default=0)),
                ('seminars_national', models.PositiveIntegerField(default=0)),
                ('seminars_international', models.PositiveIntegerField(default=0)),
                ('outreach', models.TextField()),
            ],
        ),
    ]
