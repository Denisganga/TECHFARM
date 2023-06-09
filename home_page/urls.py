from django.urls import path
from .views import MainPage,FarmOverview,Machinery,Harvestshow,Expenses,Reports,Settings,Help,add_crops,show_crops,update,delete_crop,add_animals,show_animals,update_animal,delete_animal
from home_page import views 

from django.conf import settings
from django.conf.urls.static import static

app_name='home_page'

urlpatterns = [
    # ... other URL patterns
    path('mainpage/',MainPage, name="main-page"),

    path('farmoverview/',FarmOverview,name="farm-overview"),

    path('machinery/',Machinery, name="machinery"),

    #path('livestock/',showanimals, name="livestock"),

    path('harvest/',Harvestshow, name="harvest"),

    path('expenses/',Expenses,name="expenses"),

    path('reports/', Reports, name="reports"),

    path('settings/', Settings, name="settings"),

    path('help/',Help, name="help"),


    path('create/', add_crops, name='add-crops'),

    path('harvestshow/',show_crops, name='show-crops'),

    #path('edit/<int:id>/', edit, name='edit-crops'),
    path('update/<int:id>/', update, name='update-crops'),
    path('delete/<int:id>/', delete_crop, name='delete-crops'),

   path('add/',add_animals,name='add-animals'),

   path('showanimals/',show_animals,name='show-animals'),

   path('update_animal/<int:id>/', update_animal, name='update-animal'),

   path('delete_annimal/<int:id>/', delete_animal, name='delete-animal')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)