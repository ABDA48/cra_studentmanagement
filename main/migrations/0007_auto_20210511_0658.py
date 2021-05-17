# Generated by Django 3.0.5 on 2021-05-11 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210509_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='email',
            field=models.EmailField(default='cra@gmail.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='foruser',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='university',
            name='batch',
            field=models.CharField(choices=[('1 ere annee', '1 ere annee'), ('2 eme annee', '2 eme annee'), ('3 eme annee', '3 eme annee'), ('4 eme annee', '4 eme annee'), ('5 eme annee', '5 eme annee'), ('6 eme annee', '6 eme annee')], max_length=100),
        ),
        migrations.AlterField(
            model_name='university',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
