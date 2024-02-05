# Generated by Django 4.2.7 on 2024-02-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0008_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.CharField(max_length=200, verbose_name='メールアドレス'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='お名前'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(verbose_name='メッセージ'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='タイトル'),
        ),
    ]
