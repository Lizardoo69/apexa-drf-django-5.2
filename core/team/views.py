from django.shortcuts import render

# Create your views here.

def team_view(request):
    return render(request, 'team/team.html')

def team_details_view(request):
    return render(request, 'team/team-details.html')