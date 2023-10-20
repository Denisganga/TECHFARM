from django.shortcuts import render


def MainPage(request):
    # Your view logic goes here
    return render(request,'home_page/home.html')

def Harvestshow(request):
    # Your view logic goes here
    return render(request,'home_page/harvestshow.html')

#def Expenses(request):
    # Your view logic goes here
    #return render(request,'home_page/expenses.html')

#def Reports(request):
    # Your view logic goes here
    #return render(request,'home_page/reports.html')

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


from django.contrib.auth.decorators import login_required



def add_crops(request):
    if request.method == 'POST':
        form = CropsForm(request.POST)
        if form.is_valid():

            crop = form.save(commit=False)
            crop.user = request.user

            form.save()
            return redirect('home_page:show-crops')
    else:
        form = CropsForm()
    
    return render(request, 'home_page/addcrops.html', {'form': form})

def show_crops(request):
    crops = Crops.objects.filter(user=request.user)
    
    return render(request,"home_page/harvestshow.html",{'crops':crops})
    
#def edit(request,id):
   # crops=Crops.objects.get(id=id)
    #return render(request,"home_page/edit.html",{'crops':crops})

def update(request,id):
    crops=Crops.objects.get(id=id)
    form=CropsForm(request.POST,instance=crops)

    if form.is_valid():
        form.save()
        return redirect("home_page:show-crops")
    return render(request,"home_page/update.html",{'crops':crops})

def delete_crop(request, id):
    crop = Crops.objects.get(id=id)

    if request.method == 'POST':
        crop.delete()
        return redirect('home_page:show-crops')

    return render(request, 'home_page/delete_crop.html', {'crop': crop})



#view function of the Animal AnimalsForm
from .animals_form import AnimalsForm
from .models import Animals

def add_animals(request):
    if request.method == 'POST':
        form = AnimalsForm(request.POST, request.FILES)
        if form.is_valid():

            animal = form.save(commit=False)
            animal.user = request.user
        

            form.save()
            return redirect('home_page:show-animals')
    else:
        form = AnimalsForm()

    return render(request, 'home_page/addanimals.html', {'form': form})

def show_animals(request):
    animals = Animals.objects.filter(user=request.user)

    return render (request,"home_page/showlivestock.html",{'animals':animals})

def update_animal(request, id):
    animals = Animals.objects.get(id=id)
    form = AnimalsForm(request.POST, instance=animals)

    if form.is_valid():
        form.save()
        return redirect("home_page:show-animals")
    return render(request, "home_page/update_animal.html", {'animals': animals})

def delete_animal(request,id):
    animal=Animals.objects.get(id=id)

    if request.method=='POST':
        animal.delete()
        return redirect('home_page:show-animals')
    
    return render(request, 'home_page/delete_animal.html',{'animal':animal})

        #view function of the Machinery MachineryForm
from .machinery_form import MachineryForm
from .models import Machinery

def add_machinery(request):
    if request.method == 'POST':
        form = MachineryForm(request.POST)
        if form.is_valid():


            machinery = form.save(commit=False)
            machinery.user = request.user
        

            form.save()
            return redirect('home_page:show-machinery')
    else:
        form = MachineryForm()

    return render(request, 'home_page/addmachinery.html', {'form': form})

def show_machinery(request):
    machinery = Machinery.objects.filter(user=request.user)

    return render (request,"home_page/showmachinery.html",{'machinery':machinery})

def update_machinery(request,number_plate):
     machinery=Machinery.objects.get(number_plate=number_plate)
     form=MachineryForm(request.POST,instance=machinery)
     
     if form.is_valid():
         form.save()
         return redirect("home_page:show-machinery")
     return render(request, "home_page/update_machinery.html", {'machinery': machinery})

def delete_machinery(request,number_plate):
    machinery=Machinery.objects.get(number_plate=number_plate)
    if request.method=='POST':
        machinery.delete()
        return redirect('home_page:show-machinery')
    return render(request,'home_page/delete_machinery.html',{'machinery':machinery})




#view function of the expenses
from .expenses_form import ExpensesForm
from .models import Expenses

def add_expenses(request):
    if request.method == 'POST':
        form = ExpensesForm(request.POST, request.FILES)
        if form.is_valid():


            expenses = form.save(commit=False)
            expenses.user = request.user
        

            form.save()
            return redirect('home_page:show-expenses')
    else:
        form = ExpensesForm()
    
    return render(request, 'home_page/add_expense.html', {'form': form})


def show_expenses(request):
    expenses = Expenses.objects.filter(user=request.user)

    return render(request,"home_page/show_expenses.html",{'expenses':expenses})


def update_expenses(request,Eid):
    expenses=Expenses.objects.get(Eid=Eid)
    form=ExpensesForm(request.POST,instance=expenses)

    if form.is_valid():
        form.save()
        return redirect("home_page:show-expenses")
    return render(request,"home_page/update_expenses.html",{'expenses':expenses})

def delete_expenses(request,Eid):
    expenses=Expenses.objects.get(Eid=Eid)
    if request.method=='POST':
        expenses.delete()
        return redirect("home_page:show-expenses")
    return render(request,'home_page/delete_expense.html',{'expenses':expenses})


#Reports view

from .reports_form import ReportsForm
from .models import Reports

def add_reports(request):
    if request.method=='POST':
        form=ReportsForm(request.POST,request.FILES)
        if form.is_valid():

            reports = form.save(commit=False)
            reports.user = request.user
        

            form.save()
            return redirect('home_page:show-reports')
    else:
        form=ReportsForm()

    return render(request,'home_page/add_report.html',{'form':form})

def show_reports(request):
    reports = Reports.objects.filter(user=request.user)

    return render(request,"home_page/show_report.html",{'reports':reports})

def update_reports(request,Rid):
    reports=Reports.objects.get(Rid=Rid)
    form=ReportsForm(request.POST,instance=reports)

    if form.is_valid():
        form.save()
        return redirect("home_page:show-reports")
    return render (request,"home_Page/update_reports.html",{'reports':reports})


def delete_reports(request,Rid):
    reports=Reports.objects.get(Rid=Rid)
    if request.method=='POST':
        reports.delete()
        return redirect("home_page:show-reports")
    return render (request,'home_page/delete_report.html',{'reports':reports})

    

    #view function of the Farm Overview
from .overview_form import OverviewForm
from .models import Overview


def add_overview(request):
    if request.method=='POST':
        form=OverviewForm(request.POST,request.FILES)
        if form.is_valid():

            overview = form.save(commit=False)
            overview.user = request.user
        

            form.save()
            return redirect('home_page:show-overview')
    else:
        form=OverviewForm()

    return render(request,'home_page/add_overview.html',{'form':form})


def show_overview(request):
    overview = Overview.objects.filter(user=request.user)
    return render(request,"home_page/show_overview.html",{'overview':Overview})


def update_overview(request,Fid):
    overview=Overview.objects.get(Fid=Fid)
    form=OverviewForm(request.POST,instance=overview)

    if form.is_valid():
        form.save()
        return redirect("home_page:show-overview")
    return render (request,"home_page/update_overview.html",{'overview':Overview})
    

def delete_overview(request, Fid):
    overview = Overview.objects.get(Fid=Fid)
    if request.method == 'POST':
        overview.delete()
        return redirect('home_page:show-overview')
    return render(request, 'home_page/delete_overview.html', {'overview': overview})



        #view function of the Employees

from .employees_form import EmployeesForm
from. models import Employees

def add_employees(request):
    if request.method=='POST':
        form=EmployeesForm(request.POST)
        if form.is_valid():

            employees = form.save(commit=False)
            employees.user = request.user
        

            form.save()
            return redirect('home_page:show-employees')
    else:
        form=EmployeesForm()

    return render(request,'home_page/add_employees.html',{'form':form})

def show_employees(request):
    employees = Employees.objects.filter(user=request.user)
    return render(request,"home_page/show_employees.html",{'employees':employees})


def update_employees(request,Eid):
    employees=Employees.objects.get(Eid=Eid)
    form=EmployeesForm(request.POST,instance=employees)

    if form.is_valid():
        form.save()
        return redirect("home_page:show-employees")
    return render(request,"home_page/update_employees.html",{'employees':employees})

def delete_employees(request,Eid):
    employees=Employees.objects.get(Eid=Eid)
    if request.method=='POST':
        employees.delete()
        return redirect('home_page:show-employees')
    return render(request,'home_page/delete_employees.html',{'employees':employees})


from.farmimage_form import FarmimageForm
from .models import Farmimage


def upload_image(request):
    if request.method == 'POST':
        form = FarmimageForm(request.POST, request.FILES)
        if form.is_valid():

            image = form.save(commit=False)
            image.user = request.user
        

            form.save()
            return redirect ('home_page:display-gallery')
    else:
        form = FarmimageForm()
    return render(request, 'home_page/upload_image.html', {'form': form})

def display_gallery(request):
    images = Farmimage.objects.filter(user=request.user)
    return render(request, 'home_page/display_gallery.html', {'images': images})

def delete_image(request, image_id):
    image = Farmimage.objects.get(pk=image_id)
    image.delete()
    return redirect('home_page:display-gallery')