# Generated by Django 2.2.11 on 2020-04-09 13:12

from django.db import migrations


def create_subscription_form_flag(apps, schema_editor):
    Flag = apps.get_model("waffle", "Flag")
    if not Flag.objects.filter(name="subscription_form").exists():
        Flag.objects.create(
            name="subscription_form", staff=True, note="Shows the subscription form"
        )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_create_subscription_banner_flag"),
    ]

    operations = [migrations.RunPython(create_subscription_form_flag)]