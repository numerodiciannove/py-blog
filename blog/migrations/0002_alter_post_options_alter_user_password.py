# Generated by Django 4.1 on 2023-11-20 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_time"]},
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=32),
        ),
    ]