from django.shortcuts import render






def homePage(request):
    return render(request, 'index.html')

def aboutPage(request):
    return render(request, 'about.html') 



def loginPage(request):
    return render(request, 'login.html') 