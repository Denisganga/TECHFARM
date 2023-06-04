from django.urls import path
from .views import MainPage,FarmOverview,Machinery,Livestock,Harvestshow,Expenses,Reports,Settings,Help,create_crops,show_crops,edit,update,destroy
from home_page import views 

app_name='home_page'

urlpatterns = [
    # ... other URL patterns
    path('mainpage/',MainPage, name="main-page"),

    path('farmoverview/',FarmOverview,name="farm-overview"),

    path('machinery/',Machinery, name="machinery"),

    path('livestock/',Livestock, name="livestock"),

    path('harvest/',Harvestshow, name="harvest"),

    path('expenses/',Expenses,name="expenses"),

    path('reports/', Reports, name="reports"),

    path('settings/', Settings, name="settings"),

    path('help/',Help, name="help"),


    path('create/', create_crops, name='create-crops'),

    path('harvestshow/',show_crops, name='show-crops'),

    path('edit/<int:id>/', edit, name='edit-crops'),
    path('update/<int:id>/', update, name='update-crops'),
    path('delete/<int:id>/',destroy, name='delete-crops'),

   
]