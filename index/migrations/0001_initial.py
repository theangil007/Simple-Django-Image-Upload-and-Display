# Generated by Django 4.1.1 on 2023-07-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagename', models.CharField(max_length=50)),
                ('Imagefile', models.FileField(upload_to='static/')),
            ],
        ),
    ]
