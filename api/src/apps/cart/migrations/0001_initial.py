# Generated by Django 3.1.1 on 2020-09-01 11:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("external_id", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                (
                    "value",
                    models.IntegerField(
                        null=True,
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="cart.cart",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="item",
            constraint=models.UniqueConstraint(
                fields=("external_id", "cart"), name="unique_item_in_cart"
            ),
        ),
    ]
