# Generated by Django 2.0.6 on 2021-09-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgradu', '0003_paquete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='image',
            field=models.URLField(default='https://i.postimg.cc/vTphDsSm/undraw-warning-cyit.png', max_length=800),
        ),
    ]