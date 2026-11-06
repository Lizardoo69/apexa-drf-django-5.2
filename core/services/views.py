from django.shortcuts import render

# Create your views here.

def services_view(request):
    return render(request, 'services/services.html')

def project_details_view(request):
    return render(request, 'services/project-details.html')




