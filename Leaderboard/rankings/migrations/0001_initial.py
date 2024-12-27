# Generated by Django 5.1.4 on 2024-12-26 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('grade_level', models.CharField(choices=[('G8 Boys', 'G8 Boys'), ('G8 Girls', 'G8 Girls'), ('Junior Boys', 'Junior Boys'), ('Junior Girls', 'Junior Girls'), ('Senior Boys', 'Senior Boys'), ('Senior Girls', 'Senior Girls')], max_length=20)),
                ('total_points', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-total_points', 'last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_style', models.CharField(choices=[('singles', 'Singles'), ('doubles', 'Doubles')], max_length=10)),
                ('game1_team1_score', models.IntegerField()),
                ('game1_team2_score', models.IntegerField()),
                ('game2_team1_score', models.IntegerField()),
                ('game2_team2_score', models.IntegerField()),
                ('game3_team1_score', models.IntegerField(blank=True, null=True)),
                ('game3_team2_score', models.IntegerField(blank=True, null=True)),
                ('date_played', models.DateTimeField(auto_now_add=True)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player1', to='rankings.player')),
                ('player1_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player1_partner', to='rankings.player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player2', to='rankings.player')),
                ('player2_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player2_partner', to='rankings.player')),
            ],
        ),
    ]