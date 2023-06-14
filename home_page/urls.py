from django.urls import path
from .views import MainPage,FarmOverview,Harvestshow,Expenses,Reports,Settings,Help,add_crops,show_crops,update,delete_crop,add_animals,show_animals,update_animal,delete_animal,add_machinery,show_machinery,update_machinery,delete_machinery,add_expenses,show_expenses,update_expenses,delete_expenses
from home_page import views 

from django.conf import settings
from django.conf.urls.static import static

app_name='home_page'

urlpatterns = [
    # ... other URL patterns
    path('mainpage/',MainPage, name="main-page"),

    path('farmoverview/',FarmOverview,name="farm-overview"),

    #path('machinery/',Machinery, name="machinery"),

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

   path('delete_annimal/<int:id>/', delete_animal, name='delete-animal'),

   path('add_machinery/', add_machinery, name='add-machinery'),
   path('show_machinery/', show_machinery, name='show-machinery'),
   path('update_machinery/<str:number_plate>/',update_machinery, name='update-machinery'),
   path('delete_machinery/<str:number_plate>/',delete_machinery,name="delete-machinery"),
   path('add_expenses/',add_expenses,name="add-expenses"),
   path('show_expenses/',show_expenses,name="show-expenses"),
   
    path('update_expenses/<int:Eid>/', update_expenses, name='update-expenses'),
    path('delete_expenses/<int:Eid>/',delete_expenses, name="delete-expenses")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# makes the photo to appear

