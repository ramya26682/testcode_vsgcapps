# Generated by Django 2.1.1 on 2020-09-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acrpapp', '0004_auto_20200911_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='Advisor1_Telephone',
            field=models.BigIntegerField(default=None, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Advisor1_Zip_Code',
            field=models.IntegerField(default=None, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='designapp',
            name='Advisor1_Telephone',
            field=models.BigIntegerField(default=None, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='designapp',
            name='Advisor1_Zip_Code',
            field=models.IntegerField(default=None, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='designapp',
            name='Advisor2_Zip_Code',
            field=models.CharField(blank=True, default='', max_length=13),
        ),
        migrations.AlterField(
            model_name='designapp',
            name='Upload',
            field=models.FileField(max_length=256, null=True, upload_to='media/'),
        ),
    ]
