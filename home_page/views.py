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

def Harvest(request):
    # Your view logic goes here
    return render(request,'home_page/harvest.html')

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

    



