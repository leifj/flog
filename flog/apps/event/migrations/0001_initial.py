# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import flog.apps.event.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(blank=True, default=b'Unknown', max_length=256)),
            ],
            options={
                'ordering': ['country_code'],
            },
        ),
        migrations.CreateModel(
            name='DailyEduroamEventAggregation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('realm', models.CharField(max_length=200)),
                ('visited_institution', models.CharField(max_length=200)),
                ('calling_station_id', models.CharField(max_length=128)),
                ('realm_country', models.CharField(max_length=200)),
                ('visited_country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DailyEventAggregation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('origin_name', models.CharField(max_length=200)),
                ('rp_name', models.CharField(max_length=200)),
                ('protocol', models.SmallIntegerField(choices=[(0, b'Unknown'), (1, b'WAYF'), (2, b'Discovery'), (3, b'SAML2')])),
                ('num_events', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EduroamEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField(db_index=True)),
                ('version', models.CharField(max_length=10)),
                ('calling_station_id', models.CharField(max_length=128)),
                ('successful', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EduroamRealm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realm', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('country', models.ForeignKey(blank=True, default=flog.apps.event.models.get_default_country, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_realms', to='event.Country')),
            ],
            options={
                'ordering': ['realm'],
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.URLField(db_index=True, unique=True)),
                ('is_idp', models.BooleanField(default=False)),
                ('is_rp', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['uri'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField(db_index=True)),
                ('protocol', models.SmallIntegerField(choices=[(0, b'Unknown'), (1, b'WAYF'), (2, b'Discovery'), (3, b'SAML2')])),
                ('principal', models.CharField(blank=True, max_length=128, null=True)),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_events', to='event.Entity')),
                ('rp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rp_events', to='event.Entity')),
            ],
        ),
        migrations.AddField(
            model_name='eduroamevent',
            name='realm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realm_events', to='event.EduroamRealm'),
        ),
        migrations.AddField(
            model_name='eduroamevent',
            name='visited_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_events', to='event.Country'),
        ),
        migrations.AddField(
            model_name='eduroamevent',
            name='visited_institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institution_events', to='event.EduroamRealm'),
        ),
        migrations.AlterUniqueTogether(
            name='dailyeventaggregation',
            unique_together=set([('date', 'origin_name', 'rp_name', 'protocol')]),
        ),
        migrations.AlterUniqueTogether(
            name='dailyeduroameventaggregation',
            unique_together=set([('date', 'realm', 'visited_institution', 'calling_station_id')]),
        ),
    ]
