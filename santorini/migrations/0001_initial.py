# Generated by Django 3.1.4 on 2021-01-03 04:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='com_property',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('property_manager', models.CharField(max_length=300)),
                ('property_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('default_assignee', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='community',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('community_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('ticket_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('property_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='santorini.com_property')),
            ],
        ),
        migrations.AddField(
            model_name='com_property',
            name='parent_community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='santorini.community'),
        ),
    ]