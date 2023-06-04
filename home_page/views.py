from django.shortcuts import render


def MainPage(request):
    # Your view logic goes here
    return render(request,'home_page/home.html')

def FarmOverview(request):
    # Your view logic goes here
    return render(request,'home_page/overview.html')

def Machinery(request):
    # Your view logic goes here
    return render(request, 'home_page/machinery.html')

def Livestock(request):
    # Your view logic goes here
    return render(request,'home_page/livestock.html')

def Harvestshow(request):
    # Your view logic goes here
    return render(request,'home_page/harvestshow.html')

def Expenses(request):
    # Your view logic goes here
    return render(request,'home_page/expenses.html')

def Reports(request):
    # Your view logic goes here
    return render(request,'home_page/reports.html')

def Settings(request):
    # Your view logic goes here
    return render(request,'home_page/settings.html')

def Help(request):
    # Your view logic goes here
    return render(request,'home_page/help.html')

    
#view functions of cropsforms
from django.shortcuts import render,redirect
from .cropsforms import CropsForm
from .models import Crops

def create_crops(request):
    if request.method=='POST':
        form=CropsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=CropsForm
            
    return render(request,'home_page/harvest.html',{'form':form})

def show_crops(request):
    crops=Crops.objects.all()
    
    return render(request,"home_page/harvestshow.html",{'crops':crops})
    
def edit(request,id):
    crops=Crops.objects.get(id=id)
    return render(request,"home_page/edit.html",{'crops':crops})

def update(request,id):
    crops=Crops.objects.get(id=id)
    form=CropsForm(request.POST,instance=crops)

    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"home_page/update.html",{'crops':crops})

def destroy(request,id):
    crops=Crops.objects.get(id=id)
    crops.delete()
    return redirect("/show")



