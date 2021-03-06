# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-06 20:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hp', models.IntegerField()),
                ('type_1', models.CharField(choices=[(b'Normal', b'Normal'), (b'Fire', b'Fire'), (b'Water', b'Water'), (b'Electric', b'Electric'), (b'Grass', b'Grass'), (b'Ice', b'Ice'), (b'Fighting', b'Fighting'), (b'Poison', b'Poison'), (b'Ground', b'Ground'), (b'Flying', b'Flying'), (b'Psychic', b'Psychic'), (b'Bug', b'Bug'), (b'Ghost', b'Ghost'), (b'Dragon', b'Dragon'), (b'Dark', b'Dark'), (b'Steel', b'Steel'), (b'Fairy', b'Fairy')], max_length=20)),
                ('type_2', models.CharField(blank=True, choices=[(b'Normal', b'Normal'), (b'Fire', b'Fire'), (b'Water', b'Water'), (b'Electric', b'Electric'), (b'Grass', b'Grass'), (b'Ice', b'Ice'), (b'Fighting', b'Fighting'), (b'Poison', b'Poison'), (b'Ground', b'Ground'), (b'Flying', b'Flying'), (b'Psychic', b'Psychic'), (b'Bug', b'Bug'), (b'Ghost', b'Ghost'), (b'Dragon', b'Dragon'), (b'Dark', b'Dark'), (b'Steel', b'Steel'), (b'Fairy', b'Fairy')], max_length=20, null=True)),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('sp_atk', models.IntegerField()),
                ('sp_def', models.IntegerField()),
                ('total', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('num_badges', models.IntegerField()),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerPokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=10)),
                ('poke_stats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokelist.Pokemon')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='party', to='pokelist.Trainer')),
            ],
            options={
                'ordering': ('nickname',),
            },
        ),
    ]
