from django.db import models


class Player(models.Model):
    GRADE_CHOICES = [
        ('G8 Boys', 'G8 Boys'),
        ('G8 Girls', 'G8 Girls'),
        ('Junior Boys', 'Junior Boys'),
        ('Junior Girls', 'Junior Girls'),
        ('Senior Boys', 'Senior Boys'),
        ('Senior Girls', 'Senior Girls'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=20, choices=GRADE_CHOICES)
    total_points = models.IntegerField(default=0)

    class Meta:
        ordering = ['-total_points', 'last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Match(models.Model):
    GAME_STYLE_CHOICES = [
        ('singles', 'Singles'),
        ('doubles', 'Doubles'),
    ]
    
    game_style = models.CharField(max_length=10, choices=GAME_STYLE_CHOICES)
    
    # Team 1
    player1 = models.ForeignKey(Player, related_name='matches_as_player1', on_delete=models.CASCADE)
    player1_partner = models.ForeignKey(Player, related_name='matches_as_player1_partner', 
                                      on_delete=models.CASCADE, null=True, blank=True)
    
    # Team 2
    player2 = models.ForeignKey(Player, related_name='matches_as_player2', on_delete=models.CASCADE)
    player2_partner = models.ForeignKey(Player, related_name='matches_as_player2_partner', 
                                      on_delete=models.CASCADE, null=True, blank=True)
    
    # Scores
    game1_team1_score = models.IntegerField()
    game1_team2_score = models.IntegerField()
    game2_team1_score = models.IntegerField()
    game2_team2_score = models.IntegerField()
    game3_team1_score = models.IntegerField(null=True, blank=True)
    game3_team2_score = models.IntegerField(null=True, blank=True)
    
    date_played = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate games won
        team1_wins = 0
        team2_wins = 0
        
        # Game 1
        if self.game1_team1_score > self.game1_team2_score:
            team1_wins += 1
        else:
            team2_wins += 1
            
        # Game 2
        if self.game2_team1_score > self.game2_team2_score:
            team1_wins += 1
        else:
            team2_wins += 1
            
        # Game 3 (if played)
        if self.game3_team1_score is not None and self.game3_team2_score is not None:
            if self.game3_team1_score > self.game3_team2_score:
                team1_wins += 1
            else:
                team2_wins += 1

        # Calculate points
        if team1_wins > team2_wins:
            points1 = 3 if team1_wins == 2 and team2_wins == 0 else 2
            points2 = 1
        else:
            points2 = 3 if team2_wins == 2 and team1_wins == 0 else 2
            points1 = 1

        # Update player points
        self.player1.total_points += points1
        self.player2.total_points += points2
        
        # Update partner points for doubles
        if self.game_style == 'doubles':
            self.player1_partner.total_points += points1
            self.player2_partner.total_points += points2
            self.player1_partner.save()
            self.player2_partner.save()
            
        self.player1.save()
        self.player2.save()

        super().save(*args, **kwargs)