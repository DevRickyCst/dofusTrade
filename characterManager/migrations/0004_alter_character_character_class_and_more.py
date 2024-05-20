# Generated by Django 5.0.4 on 2024-05-15 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characterManager", "0003_rename_user_id_character_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="character_class",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="characterManager.characterclass",
            ),
        ),
        migrations.AlterField(
            model_name="character",
            name="level",
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name="character",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="character",
            name="server",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to="characterManager.server",
            ),
        ),
    ]