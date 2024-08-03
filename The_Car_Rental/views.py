from django.shortcuts import render
from contact.models import Contact





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

def saveContact(request):
     try:
          
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email') 
        messagesubject=request.POST.get('messagesubject')
        message=request.POST.get('message')
        if firstname == '' or lastname == '' or email == '' or messagesubject == '' or message == '' :
            return render(request, 'Contact.html')
        contact=Contact(firstname=firstname, lastname=lastname, email=email, messagesubject=messagesubject, message=message)
        contact.save()
     except:
        print('error') 
     return render(request, 'Contact.html')


def Our_teamPage(request):
    return render(request, 'Our_Team.html') 


def blogPage(request):
    return render(request, 'Blog.html') 


def Single_postPage(request):
    return render(request, 'Single_Post.html') 

