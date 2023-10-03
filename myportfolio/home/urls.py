from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.HomeView, name="ViewHome"),
    path('portfolio_detail/<int:pk>', views.PortfolioDetailView, name="ViewPortfolioDetail")
    ]
