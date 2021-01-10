# Generated by Django 3.1.3 on 2020-11-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Miner', '0010_auto_20201122_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='repositories',
            name='amountClosedComments',
            field=models.IntegerField(null=True, verbose_name='Closed issue comments'),
        ),
        migrations.AddField(
            model_name='repositories',
            name='amountClosedReactions',
            field=models.IntegerField(null=True, verbose_name='Closed issue reactions'),
        ),
        migrations.AddField(
            model_name='repositories',
            name='amountMinedIssues',
            field=models.IntegerField(null=True, verbose_name='Closed issue reactions'),
        ),
        migrations.AddField(
            model_name='repositories',
            name='amountOpenComments',
            field=models.IntegerField(null=True, verbose_name='Open issue comments'),
        ),
        migrations.AddField(
            model_name='repositories',
            name='amountOpenReactions',
            field=models.IntegerField(null=True, verbose_name='Open issue reactions'),
        ),
        migrations.AddField(
            model_name='repositories',
            name='closedIssues',
            field=models.IntegerField(null=True, verbose_name='Closed issue'),
        ),
        migrations.AddField(
            model_name='repositories',
            name='openIssues',
            field=models.IntegerField(null=True, verbose_name='Open issue'),
        ),
    ]
