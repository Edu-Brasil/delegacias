# Generated by Django 4.2.5 on 2023-09-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delegacias", "0003_alter_delegacia_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delegacia",
            name="titulo",
            field=models.CharField(max_length=350),
        ),
    ]
