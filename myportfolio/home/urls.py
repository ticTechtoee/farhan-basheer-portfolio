from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.HomeView, name="ViewHome"),
    path('portfolio_detail', views.PortfolioDetailView, name="ViewPortfolioDetail")
    ]
