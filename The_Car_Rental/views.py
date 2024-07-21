from django.shortcuts import render






def homePage(request):
    return render(request, 'index.html')

def aboutPage(request):
    return render(request, 'about.html') 



def loginPage(request):
    return render(request, 'login.html') 



def Create_accountPage(request):
    return render(request, 'create_account.html') 



def faqPage(request):
    return render(request, 'faq.html') 


def Our_carsPage(request):
    return render(request, 'Our_Cars.html') 


def Car_detailPage(request):
    return render(request, 'Car_Details.html') 


def contactPage(request):
    return render(request, 'Contact.html') 

