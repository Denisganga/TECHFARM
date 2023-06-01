from django.urls import path
from .views import MainPage,FarmOverview,Machinery,Livestock,Harvest,Expenses,Reports,Settings,Help


app_name='home_page'

urlpatterns = [
    # ... other URL patterns
    path('mainpage/',MainPage, name="main-page"),

    path('farmoverview/',FarmOverview,name="farm-overview"),

    path('machinery/',Machinery, name="machinery"),

    path('livestock/',Livestock, name="livestock"),

    path('harvest/',Harvest, name="harvest"),

    path('expenses/',Expenses,name="expenses"),

    path('reports/', Reports, name="reports"),

    path('settings/', Settings, name="settings"),

    path('help/',Help, name="help"),

]