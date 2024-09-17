from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from Main_Hero_Section.models import Main_Hero_Section
from Default_Background.models import Default_Background
from Main_Cars_Carousel.models import Main_Cars_Carousel
from Counter_Section.models import Counter_Section
from Why_Choose_Us_Section.models import Why_Choose_Us_Section
from Testimonial.models import Testimonial
from Background_Video.models import Background_Video
from Our_Team.models import Our_Team
from General_Questions.models import General_Questions
from CARS.models import CARS
from contact.models import Contact
from Quick_Book.models import Quick_Book
from Blog.models import Blog
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as user_login ,logout
from About_Counter_Description.models import About_Counter_Description
from Book_Your_Drive_Section.models import Book_Your_Drive
from Questions_About_Payment.models import Payment_Questions
from cart.cart import Cart
from datetime import datetime
from users.models import UserProfile
from Header.models import Header
from django.core.mail import send_mail
from Header.models import Header
from Footer.models import Footer





def homePage(request):
    header = Header.objects.all()
    Main_Hero_Section_Data = Main_Hero_Section.objects.all()
    Main_Cars_Carousel_Data = Main_Cars_Carousel.objects.all()
    Counter_Section_Data= Counter_Section.objects.all()
    Why_Choose_Us_Section_Data = Why_Choose_Us_Section.objects.all()
    Cars_Data = CARS.objects.all()
    Testimonial_Data = Testimonial.objects.all()
    Background_Video_Data = Background_Video.objects.all()
    Blog_Data = Blog.objects.all()
    General_Questions_Data = General_Questions.objects.all()
    footer= Footer.objects.all()

    Data= {
        "header_data": header,
        "main_Hero_Section":Main_Hero_Section_Data,
        "main_Cars_Carousel":Main_Cars_Carousel_Data,
        "counter_Section":Counter_Section_Data,
        "why_Choose_Us_Section":Why_Choose_Us_Section_Data,
        "Car_Data": Cars_Data,
        "Testimonial": Testimonial_Data,
        "Background_Video": Background_Video_Data,
        "Latest_Blog": Blog_Data,
        "General_Questions" : General_Questions_Data,
        "footer_data":footer,    
    }
    return render(request, 'index.html', Data)




def addyourCarPage(request):
    Default_Background_Data = Default_Background.objects.all()
    Data= {
            "default_background":Default_Background_Data,
    }
    return render(request, 'Add-Your-Car.html',Data)



def addyourCar(request):

    if request.method == 'POST':
        name = request.POST.get('name', '')
        passengers = request.POST.get('passengers', '')
        pod = request.POST.get('pod', '')
        aom = request.POST.get('aom', '')
        description = request.POST.get('description', '')

        if not all([name, passengers, pod, aom, description]):
            print("error")

            return redirect('addyourcar')

        try:
            addcar = CARS(
                name=name,
                passengers=passengers,
                pod=pod,
                aom=aom,
                description=description
            )
            addcar.save()
            messages.success(request, "Success! Your message has been sent.")
            return redirect('home')

        except Exception as e:
            print(f"Error saving contact: {e}")
            print("ERROr")
            return redirect('addyourcar')
            
    return redirect('addyourcar')



 


def aboutPage(request):
    header = Header.objects.all()
    Default_Background_Data = Default_Background.objects.all()
    Main_Cars_Carousel_Data = Main_Cars_Carousel.objects.all()
    Counter_Section_Data= Counter_Section.objects.all()
    Counter_Description_Data= About_Counter_Description.objects.all()
    Book_your_drive = Book_Your_Drive.objects.all()
    top_items = Our_Team.objects.all()[:3] 
    footer= Footer.objects.all()   
    Data={
        "header_data": header,
        "default_background":Default_Background_Data,
        "main_Cars_Carousel":Main_Cars_Carousel_Data,
        "counter_Section":Counter_Section_Data,
        "About_Description": Counter_Description_Data,
        "Book_Your_Drive_Section": Book_your_drive,
        'top_3_cards': top_items,
        "footer_data":footer,   
    }

    return render(request, 'about.html', Data) 







def loginPage(request):
    header = Header.objects.all()
    Default_Background_Data = Default_Background.objects.all()
    footer= Footer.objects.all()  
    Data={
        "header_data": header,
        "default_background":Default_Background_Data,
        "footer_data":footer,   
    }
    if request.user.is_authenticated:
       return redirect('home')
    return render(request, 'login.html', Data) 


def Create_accountPage(request):
    header = Header.objects.all()
    Default_Background_Data = Default_Background.objects.all()
    footer= Footer.objects.all() 
    Data={
        "header_data": header,
        "default_background":Default_Background_Data,
        "footer_data":footer, 
    }
    return render(request, 'create_account.html', Data) 


def Create_accountPageUser(request): 
    uname = request.POST['username']
    uemail = request.POST['email']
    upassword = request.POST['password']

    if uname == '' or uemail == '' or upassword == ''  :
        messages.error(request, "Please fill all fields.")
        return redirect('create_account')

    if len(upassword) != 8:
        messages.error(request, "Password must be exactly 8 characters long.")
        return redirect('create_account')


        
    user = User.objects.create_user(username=uname, email=uemail, password=upassword)
    return render(request, 'login.html')


def loginUser(request):
    
    uname = request.POST['username']
    upassword = request.POST['password']

    if uname == '' or upassword == ''  :
        messages.error(request, "Please provide ther username and password")
        return redirect('login')
    user = authenticate(request, username=uname, password=upassword)
  
    if user is not None:
         user_login(request, user)
         request.session['username'] = user.username
         request.session['password'] = user.password
         return redirect('/')
    else:
        messages.error(request, "User does not exit")
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')




def faqPage(request):
    header = Header.objects.all()
    Default_Background_Data = Default_Background.objects.all()
    General_Questions_Data = General_Questions.objects.all()
    Payment_Questions_Data = Payment_Questions.objects.all()
    footer= Footer.objects.all()  
    Data={
        "header_data": header,
        "General_Questions" : General_Questions_Data,
        "Payment_questions" : Payment_Questions_Data,  
        "default_background":Default_Background_Data,
        "footer_data":footer,   
    }
    return render(request, 'faq.html', Data) 


def Our_carsPage(request):
    header = Header.objects.all()
    Default_Background_Data = Default_Background.objects.all()
    Cars_Data = CARS.objects.all()
    Cars_Data= Paginator(Cars_Data, 6)
    page = request.GET.get('page')
    products = Cars_Data.get_page(page)
    totalpages = [x+1 for x in range(Cars_Data.num_pages)]
    Background_Video_Data = Background_Video.objects.all()
    Blog_Data = Blog.objects.all()
    footer= Footer.objects.all()  
    Data= {
        "header_data": header,
        "default_background":Default_Background_Data,
        "cars_Section": products,
        "total_Pages": totalpages,
        "Background_Video":Background_Video_Data,
        "Latest_Blog": Blog_Data,
        "footer_data":footer,   
    }
    return render(request, 'Our_Cars.html', Data) 




def Car_detailPage(request, id):
    header = Header.objects.all()
    Default_Background_Data = Default_Background.objects.all()
    Cars_Data = CARS.objects.all()
    Car_1 = CARS.objects.get(id__exact=id)
    footer= Footer.objects.all()  
    Data = {
        "header_data": header,
        "default_background":Default_Background_Data,
        "Car_Data": Cars_Data,
        "One_Car": Car_1,
        "current_id": int(id),
        "footer_data":footer,  
    }
    return render(request, 'Car_Details.html', Data) 


def reservationPage(request, id):
    header = Header.objects.all()
    Cars_Data = CARS.objects.all()
    Cars_Data= Paginator(Cars_Data, 6)
    page = request.GET.get('page')
    products = Cars_Data.get_page(page)
    Car_1 = CARS.objects.get(id__exact=id)
    footer= Footer.objects.all()  
    Data = {
        "header_data": header,
        "cars_Section": products,
        "One_Car": Car_1,
        "current_id_2": int(id),
        "footer_data":footer,  
    }
    return render(request, 'Reservation.html', Data) 

# def checkoutPage(request):
#     cart= Cart(request)
#     bookings_total = 0
#     bookings= list(cart.session.values())[5]
#     for book in bookings:
#         bookings_total = bookings_total + int(bookings[book]["quantity"])

#     items= list(cart.session.values())[5]
#     subtotal = 0
#     for item in items:
#         subtotal = subtotal + int(items[item]['price'])*items[item]['quantity']
#     Data = {
#         "subtotal": subtotal,
#         "bookings":bookings_total
#     }
#     return render(request, 'Checkout.html', Data) 

def checkout_view(request):
    header = Header.objects.all()
    footer= Footer.objects.all()  
    cart = request.session.get('cart', {})
    subtotal = sum(float(item['price']) * item['quantity'] for item in cart.values())

    
    rental_days = 1  
    if request.method == 'POST':
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        if pickup_date and return_date:
            pickup_date = datetime.strptime(pickup_date, '%Y-%m-%d')
            return_date = datetime.strptime(return_date, '%Y-%m-%d')
            rental_days = (return_date - pickup_date).days
    
    context = {
        "header_data": header,
        'subtotal': subtotal,
        'Rental_days': rental_days,
        "footer_data":footer,  
    }
    return render(request, 'checkout.html', context)




def process_checkout(request):
    if request.method == 'POST':
        user = request.user
        

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        postal_code = request.POST.get('postal_code')
        address_line_1 = request.POST.get('address_line_1')
        address_line_2 = request.POST.get('address_line_2')
        province = request.POST.get('province')
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        phone = request.POST.get('phone')
        email = request.POST.get('email')


        user.first_name = first_name
        user.last_name = last_name
        user.adress_line_1 = address_line_1
        user.adress_line_2 = address_line_2
        user.pickup_date = pickup_date
        user._date = return_date
        user.email = email
        user.save()

        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.phone = phone
        profile.address_line_1 = address_line_1
        profile.address_line_2 = address_line_2
        profile.postal_code = postal_code
        profile.province = province
        profile.pickup_date = pickup_date
        profile.return_date = return_date
        profile.save()

        
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')  
        request.session['cart'] = {}

        return redirect('order_confirmation')

    return redirect('checkout')





# def contactPage(request):
#     return render(request, 'Contact.html') 

# def saveContact(request):
#      try:
          
#         firstname=request.POST.get('firstname')
#         lastname=request.POST.get('lastname')
#         email=request.POST.get('email') 
#         messagesubject=request.POST.get('messagesubject')
#         message=request.POST.get('message')
#         if firstname == '' or lastname == '' or email == '' or messagesubject == '' or message == '' :
#             messages.error(request, "Not found. Please fill all fields.") 
#             return render(request, 'Contact.html')
#         contact=Contact(firstname=firstname, lastname=lastname, email=email, messagesubject=messagesubject, message=message)
#         messages.success(request, "Success! Your message has been sent.")
#         contact.save()
#      except:
#         print('error') 
#      return render(request, 'Contact.html')

def contactPage(request):
    header = Header.objects.all()
    Default_Background_Data = Default_Background.objects.all()
    General_Questions_Data = General_Questions.objects.all()
    footer= Footer.objects.all()  
    Data={
        "header_data": header,
        "default_background":Default_Background_Data,
        "General_Questions" : General_Questions_Data,
        "footer_data":footer,     
    }
    return render(request, 'Contact.html', Data) 

def saveContact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        messagesubject = request.POST.get('messagesubject', '')
        message = request.POST.get('message', '')

        if not all([firstname, lastname, email, messagesubject, message]):
            messages.error(request, "Please fill all fields.")
            return redirect('contactPage')

        try:
            contact = Contact(
                firstname=firstname,
                lastname=lastname,
                email=email,
                messagesubject=messagesubject,
                message=message
            )
            contact.save()
            messages.success(request, "Success! Your message has been sent.")
            return redirect('contactPage')

        except Exception as e:
            print(f"Error saving contact: {e}")
            messages.error(request, "An error occurred. Please try again.")
            return redirect('contactPage')
            

    return redirect('contactPage')



def Our_teamPage(request):
    header = Header.objects.all()
    Default_Background_Data = Default_Background.objects.all()
    Team_Cards = Our_Team.objects.all()
    Background_Video_Data = Background_Video.objects.all()
    Testimonial_Data = Testimonial.objects.all()
    footer= Footer.objects.all() 
    Data={
        "header_data": header,
        "default_background":Default_Background_Data,
        "Team_Cards_Data":Team_Cards,
        "Background_Video":Background_Video_Data,
        "Testimonial": Testimonial_Data,
        "footer_data":footer,  
    }
    return render(request, 'Our_Team.html',Data) 


def blogPage(request):
    header = Header.objects.all()
    Default_Background_Data = Default_Background.objects.all()
    footer= Footer.objects.all() 
    Blog_Data = Blog.objects.all()
    Blog_Data= Paginator(Blog_Data, 6)
    page = request.GET.get('page')
    products = Blog_Data.get_page(page)
    totalpages = [x+1 for x in range(Blog_Data.num_pages)]
    Data = {
        "header_data": header,
        "default_background":Default_Background_Data,
        "Blog":products,
        "total_Pages": totalpages,
        "footer_data":footer,  
    }
    return render(request, 'Blog.html',Data) 


def Single_postPage(request, id):
    header = Header.objects.all()
    blog = Blog.objects.get(id__exact=id)
    footer= Footer.objects.all() 
    Data = {
        "header_data": header,
        "One_Blog": blog,
        "footer_data":footer, 
    }
    return render(request, 'Single_Post.html', Data) 















def cart_add(request, id):
    cart = Cart(request)
    product = CARS.objects.get(id=id)
    cart.add(product=product)
    return redirect("reservation")



def item_clear(request, id):
    cart = Cart(request)
    product = CARS.objects.get(id=id)
    cart.remove(product)
    return redirect("reservation")



def item_increment(request, id):
    cart = Cart(request)
    product = CARS.objects.get(id=id)
    cart.add(product=product)
    return redirect("reservation")



def item_decrement(request, id):
    cart = Cart(request)
    product = CARS.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("reservation")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("reservation")



# def cart_detail(request):
#     cart= Cart(request)
#     bookings_total = 0
#     bookings= list(cart.session.values())[5]
#     for book in bookings:
#         bookings_total = bookings_total + int(bookings[book]["quantity"])

#     items= list(cart.session.values())[5]
#     subtotal = 0
#     for item in items:
#         subtotal = subtotal + int(items[item]['price'])*items[item]['quantity']
#     Data = {
#         "subtotal": subtotal,
#         "bookings": bookings_total
#     }
#     return render(request, 'Reservation.html', Data)
def cart_detail(request):
    header = Header.objects.all()
    footer= Footer.objects.all() 
    cart = Cart(request)
    bookings_total = 0

    session_values = list(cart.session.values())

    # Check if there are enough items in session values
    if len(session_values) > 5:
        bookings = session_values[5]
    else:
        bookings = []  # Jab 6 items nahi milte, bookings ko empty list set karo

    # Only calculate bookings_total if there are bookings
    if bookings:
        for book in bookings:
            bookings_total = bookings_total + int(bookings[book]["quantity"])

    # Check if there are enough items in session values for items as well
    if len(session_values) > 5:
        items = session_values[5]
    else:
        items = []  # Jab 6 items nahi milte, to items ko empty list set karo

    subtotal = 0
    if items:  # Only calculate if items exist
        for item in items:
            subtotal = subtotal + int(items[item]['price']) * items[item]['quantity']

    Data = {
        "header_data": header,
        "subtotal": subtotal,
        "bookings": bookings_total,
        "footer_data":footer, 
    }

    return render(request, 'Reservation.html', Data)















def successPage(request):
    return render(request, 'Success.html')




def cancelPage(request):
    return render(request, 'Cancel.html')




def Booking_Failed_Page(request):
    return render(request, 'Booking_Failed.html')




def Booking_Corfirmed_Page(request):
    return render(request, 'Quick_Booking_Confirmed.html')





















def quick_Book(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        car = request.POST.get('car_name_dropdown', '') 
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')

        if not all([name, car, phone, email]):
            return redirect('Booking-Failed')

        try:
            contact = Quick_Book(
                name=name,
                car=car,
                phone=phone,
                email=email
            )
            contact.save()
            '''send_mail(
                'Your Booking Confirmation',
                f'Hello {Quick_Book.name},\n\nThank you for your booking.\n\nMessage: hi hi',
                'malikqasim20051@gmail.com',  # Replace with your from email address
                [Quick_Book.email],
                fail_silently=False,
            )'''
            return redirect('Booking-Confirmed')


        except Exception as e:
            return redirect('Booking-Failed')
            



    return redirect('home')




