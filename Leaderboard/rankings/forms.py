from django import forms
from .models import Match, Player


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = [
            'game_style',
            'player1', 
            'player1_partner',
            'player2',
            'player2_partner',
            'game1_team1_score', 
            'game1_team2_score',
            'game2_team1_score', 
            'game2_team2_score',
            'game3_team1_score', 
            'game3_team2_score',
        ]
        widgets = {
            'player1': forms.Select(attrs={
                'class': 'select-player',
                'required': True
            }),
            'player1_partner': forms.Select(attrs={
                'class': 'select-player doubles-only',
                'required': False
            }),
            'player2': forms.Select(attrs={
                'class': 'select-player',
                'required': True
            }),
            'player2_partner': forms.Select(attrs={
                'class': 'select-player doubles-only',
                'required': False
            }),
            'game1_team1_score': forms.NumberInput(attrs={
                'class': 'score-input',
                'min': 0,
                'required': True
            }),
            'game1_team2_score': forms.NumberInput(attrs={
                'class': 'score-input',
                'min': 0,
                'required': True
            }),
            'game2_team1_score': forms.NumberInput(attrs={
                'class': 'score-input',
                'min': 0,
                'required': True
            }),
            'game2_team2_score': forms.NumberInput(attrs={
                'class': 'score-input',
                'min': 0,
                'required': True
            }),
            'game3_team1_score': forms.NumberInput(attrs={
                'class': 'score-input',
                'min': 0,
                'required': False,
                'placeholder': 'Optional'
            }),
            'game3_team2_score': forms.NumberInput(attrs={
                'class': 'score-input',
                'min': 0,
                'required': False,
                'placeholder': 'Optional'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        player_choices = []
        for grade in Player.GRADE_CHOICES:
            players = Player.objects.filter(grade_level=grade[0]).order_by('last_name', 'first_name')
            if players:
                player_choices.append((grade[0], [(p.id, f"{p.first_name} {p.last_name}") for p in players]))
        
        empty_choice = [('', '---------')]
        for field in ['player1', 'player1_partner', 'player2', 'player2_partner']:
            self.fields[field].choices = empty_choice + [(group, players) for group, players in player_choices]

    def clean(self):
        cleaned_data = super().clean()
        game_style = cleaned_data.get('game_style')
        player1_partner = cleaned_data.get('player1_partner')
        player2_partner = cleaned_data.get('player2_partner')

        if game_style == 'doubles':
            if not player1_partner:
                raise forms.ValidationError("Player 1's partner is required for doubles matches")
            if not player2_partner:
                raise forms.ValidationError("Player 2's partner is required for doubles matches")
        else:
            cleaned_data['player1_partner'] = None
            cleaned_data['player2_partner'] = None

        # Check that all players are different
        players = [
            cleaned_data.get('player1'),
            cleaned_data.get('player2'),
            player1_partner,
            player2_partner
        ]
        players = [p for p in players if p is not None]
        if len(set(players)) != len(players):
            raise forms.ValidationError("All players must be different")

        return cleaned_data