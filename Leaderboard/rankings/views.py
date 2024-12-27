from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import Player, Match
from .forms import MatchForm
from django.utils import timezone

class LeaderboardView(ListView):
    model = Player
    template_name = 'rankings/leaderboard.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.all().order_by('grade_level', '-total_points', 'last_name', 'first_name')

def record_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            match.save()
            messages.success(request, 'Match recorded successfully!')
            return redirect('leaderboard')
    else:
        form = MatchForm()
    return render(request, 'rankings/record_match.html', {'form': form})