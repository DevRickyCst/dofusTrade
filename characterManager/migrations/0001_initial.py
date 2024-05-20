# Generated by Django 5.0.4 on 2024-05-20 13:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("itemViewer", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CharacterClass",
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
                (
                    "name",
                    models.CharField(
                        default="random", max_length=100, unique=True
                    ),
                ),
                (
                    "logo_url",
                    models.CharField(default="random", max_length=100),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Server",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SetCaracteristique",
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
                ("vitalite", models.IntegerField(default=0)),
                ("sagesse", models.IntegerField(default=0)),
                ("agilite", models.IntegerField(default=0)),
                ("intelligence", models.IntegerField(default=0)),
                ("chance", models.IntegerField(default=0)),
                ("force", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Character",
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
                ("name", models.CharField(max_length=100)),
                ("level", models.IntegerField(default=200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "character_class",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="characterManager.characterclass",
                    ),
                ),
                (
                    "server",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="characterManager.server",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SetStuff",
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
                (
                    "anneau_1",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stuffset_anneau_1",
                        to="itemViewer.item",
                    ),
                ),
                (
                    "anneau_2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stuffset_anneau_2",
                        to="itemViewer.item",
                    ),
                ),
                (
                    "arme",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stuffset_arme",
                        to="itemViewer.item",
                    ),
                ),
                (
                    "botte",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stuffset_botte",
                        to="itemViewer.item",
                    ),
                ),
                (
                    "bouclier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stuffset_bouclier",
                        to="itemViewer.item",
                    ),
                ),
                (
                    "ceinture",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stuffset_ceinture",
                        to="itemViewer.item",
                    ),
                ),
                (
                    "chapeau",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stuffset_chapeau",
                        to="itemViewer.item",
                    ),
                ),
                (
                    "collier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stuffset_collier",
                        to="itemViewer.item",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Set",
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
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="characterManager.character",
                    ),
                ),
                (
                    "caracteristique",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="characterManager.setcaracteristique",
                    ),
                ),
                (
                    "stuff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="characterManager.setstuff",
                    ),
                ),
            ],
        ),
    ]
