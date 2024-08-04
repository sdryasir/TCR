from django.shortcuts import render, redirect
from contact.models import Contact
from django.core.paginator import Paginator
from Main_Hero_Section.models import Main_Hero_Section
from Main_Cars_Carousel.models import Main_Cars_Carousel
from Counter_Section.models import Counter_Section
from Why_Choose_Us_Section.models import Why_Choose_Us_Section
from Choose_Car_Options.models import Choose_Car_Options
from Featured_Cars.models import Featured_Cars
from Cars.models import Cars



def homePage(request):
    Main_Hero_Section_Data = Main_Hero_Section.objects.all()
    Choose_Car_Options_Data = Choose_Car_Options.objects.all()
    Main_Cars_Carousel_Data = Main_Cars_Carousel.objects.all()
    Counter_Section_Data= Counter_Section.objects.all()
    Why_Choose_Us_Section_Data = Why_Choose_Us_Section.objects.all()
    Featured_Cars_Data= Featured_Cars.objects.all()

    Data= {
        "main_Hero_Section":Main_Hero_Section_Data,
        "choose_Car_Option":Choose_Car_Options_Data,
        "main_Cars_Carousel":Main_Cars_Carousel_Data,
        "counter_Section":Counter_Section_Data,
        "why_Choose_Us_Section":Why_Choose_Us_Section_Data,
        "featured_cars_Section":Featured_Cars_Data,
    }


    return render(request, 'index.html', Data)












def aboutPage(request):
    return render(request, 'about.html') 



def loginPage(request):
    return render(request, 'login.html') 



def Create_accountPage(request):
    return render(request, 'create_account.html') 



def faqPage(request):
    return render(request, 'faq.html') 


def Our_carsPage(request):
    Cars_Data = Cars.objects.all()
    Cars_Data= Paginator(Cars_Data, 6)
    page = request.GET.get('page')
    products = Cars_Data.get_page(page)
    totalpages = [x+1 for x in range(Cars_Data.num_pages)]
    Data= {
        "cars_Section": products,
        "total_Pages": totalpages,
    }
    return render(request, 'Our_Cars.html', Data) 














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





