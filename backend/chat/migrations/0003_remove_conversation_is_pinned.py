# Generated by Django 5.0.2 on 2025-03-13 12:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_conversation_is_pinned_conversation_summary"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="conversation",
            name="is_pinned",
        ),
    ]
