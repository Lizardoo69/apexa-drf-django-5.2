from django.shortcuts import render

# Create your views here.

def services_view(request):
    return render(request, 'services/services.html')

def services_details_view(request):
    return render(request, 'services/project-details.html')