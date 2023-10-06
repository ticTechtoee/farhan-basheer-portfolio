from django.shortcuts import render
from .models import Projects

def HomeView(request):
    project = Projects.objects.all()

    # Email Sending Function
     

    context = {'all_projects': project}
    return render(request,'home/index.html', context)

def PortfolioDetailView(request, pk):
    Project_Detail = Projects.objects.get(id=pk)
    context = {'Project':Project_Detail}
    return render(request,'home/portfolio-details.html', context)
