# Generated by Django 4.2.5 on 2023-09-15 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delegacias", "0005_alter_delegacia_titulo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Regiao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("criacao", models.DateTimeField(auto_created=True)),
                ("atualizacao", models.DateTimeField(auto_now=True)),
                ("ativo", models.BooleanField(default=True)),
                ("cidade", models.CharField(max_length=255)),
                ("cep", models.CharField(max_length=10)),
            ],
            options={
                "verbose_name": "Regiao",
                "verbose_name_plural": "Regioes",
            },
        ),
    ]
