# Generated by Django 5.0.1 on 2024-03-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_radiologists_dicomdata_radiologist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExportList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('export', models.CharField(max_length=255, verbose_name='export')),
            ],
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='exportlist',
            field=models.ManyToManyField(to='users.exportlist'),
        ),
    ]
