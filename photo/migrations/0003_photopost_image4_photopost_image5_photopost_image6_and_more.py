# Generated by Django 4.1.7 on 2023-05-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photopost_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopost',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ4'),
        ),
        migrations.AddField(
            model_name='photopost',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ5'),
        ),
        migrations.AddField(
            model_name='photopost',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ6'),
        ),
        migrations.AddField(
            model_name='photopost',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ7'),
        ),
        migrations.AddField(
            model_name='photopost',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ8'),
        ),
        migrations.AddField(
            model_name='photopost',
            name='image9',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ9'),
        ),
    ]
