from django.urls import path
from .views import MainPage,Harvestshow,Settings,Help,add_crops,show_crops,update,delete_crop,add_animals,show_animals,update_animal,delete_animal,add_machinery,show_machinery,update_machinery,delete_machinery,add_expenses,show_expenses,update_expenses,delete_expenses,add_reports,show_reports,update_reports,delete_reports,add_overview,show_overview,update_overview,delete_overview,add_employees,show_employees,update_employees,delete_employees,upload_image,display_gallery,delete_image
from home_page import views 

from django.conf import settings
from django.conf.urls.static import static

app_name='home_page'

urlpatterns = [
    # ... other URL patterns
    path('mainpage/',MainPage, name="main-page"),

    path('harvest/',Harvestshow, name="harvest"),

    #path('expenses/',Expenses,name="expenses"),

    path('settings/', Settings, name="settings"),

    path('help/',Help, name="help"),


    path('create/', add_crops, name='add-crops'),

    path('harvestshow/',show_crops, name='show-crops'),

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
    path('delete_expenses/<int:Eid>/',delete_expenses, name="delete-expenses"),


    path('add_reports/',add_reports, name='add-reports'),
    path('show_reports/', show_reports, name="show-reports"),
    path('update_reports/<int:Rid>/',update_reports, name="update-reports"),
    path('delete_reports/<int:Rid>/',delete_reports, name="delete-reports" ),


    path('add_overview/',add_overview, name="add-overview"),
    path('show_overview/', show_overview, name="show-overview"),
    path('update_overview/<int:Fid>/',update_overview, name="update-overview"),
    path('delete_overview/<int:Fid>/',delete_overview, name="delete-overview"),


    path('add_employees/',add_employees,name="add-employees"),
    path('show_employees/',show_employees, name="show-employees"),
    path('update_employees/<int:Eid>/',update_employees, name="update-employees"),
    path('delete_employees/<int:Eid>/',delete_employees,name="delete-employees"),


    path('upload_image/',upload_image, name="upload-image"),
    path('display_gallery/', display_gallery,name="display-gallery"),
    path('delete_image/<int:image_id>/',delete_image,name="delete-image")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# makes the photo to appear

