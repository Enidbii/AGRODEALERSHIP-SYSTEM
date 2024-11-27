# Generated by Django 5.1.2 on 2024-11-11 11:38

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0014_auto_20241107_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated at')),
                ('app_name', models.CharField(max_length=150)),
                ('consumer_key', models.CharField(max_length=250)),
                ('consumer_secret', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usermanage.state')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]