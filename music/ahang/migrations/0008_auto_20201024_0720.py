# Generated by Django 3.1.2 on 2020-10-24 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahang', '0007_ahang_isagreed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahang',
            name='ahang_esm',
            field=models.CharField(default='بی اسم', max_length=500),
        ),
    ]
