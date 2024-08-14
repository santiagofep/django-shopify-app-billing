# Generated by Django 4.2.1 on 2024-08-14 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    operations = [
        migrations.CreateModel(
            name="ShopBilling",
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
                    "shop",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing",
                        to="shops.shop",
                    ),
                ),
            ],
            options={
                "verbose_name": "Shop Billing",
                "verbose_name_plural": "Shops Billing",
            },
        ),
        migrations.CreateModel(
            name="RecurringApplicationCharge",
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
                ("shopify_rest_id", models.BigIntegerField(default=None)),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("status", models.CharField(max_length=255)),
                ("test", models.BooleanField(default=False)),
                ("currency", models.CharField(max_length=255)),
                (
                    "shop_billing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recurring_application_charges",
                        to="shopify_app_billing.shopbilling",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="recurringapplicationcharge",
            constraint=models.UniqueConstraint(
                fields=("shop_billing", "shopify_rest_id"),
                name="unique_shop_billing_shopify_rest_id",
            ),
        ),
    ]
