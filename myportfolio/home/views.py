from django.shortcuts import render
from .models import Projects

def HomeView(request):
    project = Projects.objects.all()
    context = {'all_projects': project}
    return render(request,'home/index.html', context)

def PortfolioDetailView(request):
    return render(request,'home/portfolio-details.html')
