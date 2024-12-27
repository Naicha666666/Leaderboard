from django.contrib import admin
from .models import Player, Match

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'grade_level', 'total_points')
    list_filter = ('grade_level',)
    search_fields = ('first_name', 'last_name')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('date_played', 'game_style', 'player_names', 'game1_score', 'game2_score', 'game3_score')
    list_filter = ('game_style', 'date_played')

    def player_names(self, obj):
        if obj.game_style == 'singles':
            return f"{obj.player1} vs {obj.player2}"
        else:
            return f"{obj.player1}/{obj.player1_partner} vs {obj.player2}/{obj.player2_partner}"
    player_names.short_description = 'Players'

    def game1_score(self, obj):
        return f"{obj.game1_team1_score}-{obj.game1_team2_score}"
    game1_score.short_description = 'Game 1'

    def game2_score(self, obj):
        return f"{obj.game2_team1_score}-{obj.game2_team2_score}"
    game2_score.short_description = 'Game 2'

    def game3_score(self, obj):
        if obj.game3_team1_score is not None and obj.game3_team2_score is not None:
            return f"{obj.game3_team1_score}-{obj.game3_team2_score}"
        return "Not Played"
    game3_score.short_description = 'Game 3'