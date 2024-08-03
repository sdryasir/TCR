from django.shortcuts import render
from Main_Hero_Section.models import Main_Hero_Section
from Main_Cars_Carousel.models import Main_Cars_Carousel




def homePage(request):
    Main_Hero_Section_Data = Main_Hero_Section.objects.all()
    Main_Cars_Carousel_Data = Main_Cars_Carousel.objects.all()

    Data= {
        "Main_Hero_Section_Data":Main_Hero_Section_Data,
        "Main_Cars_Carousel":Main_Cars_Carousel_Data
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
    return render(request, 'Our_Cars.html') 


def Car_detailPage(request):
    return render(request, 'Car_Details.html') 


def contactPage(request):
    return render(request, 'Contact.html') 


def Our_teamPage(request):
    return render(request, 'Our_Team.html') 


def blogPage(request):
    return render(request, 'Blog.html') 


def Single_postPage(request):
    return render(request, 'Single_Post.html') 





