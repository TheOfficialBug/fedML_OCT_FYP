# Generated by Django 4.1 on 2023-04-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client_model_weights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('model_weights', models.JSONField(default=list)),
            ],
        ),
    ]
