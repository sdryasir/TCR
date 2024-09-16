from django.shortcuts import render, redirect , get_object_or_404
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
import stripe
from django.conf import settings
from orders.models import Order
from datetime import timedelta
from django.utils import timezone
from users.models import UserProfile
from django.http import JsonResponse
from orders.forms import OrderForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView


def homePage(request):

    Main_Hero_Section_Data = Main_Hero_Section.objects.all()
    Main_Cars_Carousel_Data = Main_Cars_Carousel.objects.all()
    Counter_Section_Data= Counter_Section.objects.all()
    Why_Choose_Us_Section_Data = Why_Choose_Us_Section.objects.all()
    Cars_Data = CARS.objects.all()
    Testimonial_Data = Testimonial.objects.all()
    Background_Video_Data = Background_Video.objects.all()
    Blog_Data = Blog.objects.all()
    General_Questions_Data = General_Questions.objects.all()

    Data= {
        "main_Hero_Section":Main_Hero_Section_Data,
        "main_Cars_Carousel":Main_Cars_Carousel_Data,
        "counter_Section":Counter_Section_Data,
        "why_Choose_Us_Section":Why_Choose_Us_Section_Data,
        "Car_Data": Cars_Data,
        "Testimonial": Testimonial_Data,
        "Background_Video": Background_Video_Data,
        "Latest_Blog": Blog_Data,
        "General_Questions" : General_Questions_Data     
    }
    return render(request, 'index.html', Data)


 


def aboutPage(request):
    Default_Background_Data = Default_Background.objects.all()
    Main_Cars_Carousel_Data = Main_Cars_Carousel.objects.all()
    Counter_Section_Data= Counter_Section.objects.all()
    Counter_Description_Data= About_Counter_Description.objects.all()
    Book_your_drive = Book_Your_Drive.objects.all()
    top_items = Our_Team.objects.all()[:3]    
    Data={
        "default_background":Default_Background_Data,
        "main_Cars_Carousel":Main_Cars_Carousel_Data,
        "counter_Section":Counter_Section_Data,
        "About_Description": Counter_Description_Data,
        "Book_Your_Drive_Section": Book_your_drive,
        'top_3_cards': top_items
    }

    return render(request, 'about.html', Data) 







def loginPage(request):
    Default_Background_Data = Default_Background.objects.all()
    Data={
        "default_background":Default_Background_Data,
    }
    if request.user.is_authenticated:
       return redirect('home')
    return render(request, 'login.html', Data) 


def Create_accountPage(request):
    Default_Background_Data = Default_Background.objects.all()
    Data={
        "default_background":Default_Background_Data,
    }
    return render(request, 'create_account.html', Data) 


def Create_accountPageUser(request): 
    uname = request.POST['username']
    uemail = request.POST['email']
    upassword = request.POST['password']

    if uname == '' or uemail == '' or upassword == ''  :
        messages.error(request, "Please fill all fields.")
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
    Default_Background_Data = Default_Background.objects.all()
    General_Questions_Data = General_Questions.objects.all()
    Payment_Questions_Data = Payment_Questions.objects.all()
    Data={
        "General_Questions" : General_Questions_Data,
        "Payment_questions" : Payment_Questions_Data,  
        "default_background":Default_Background_Data,
    }
    return render(request, 'faq.html', Data) 


def Our_carsPage(request):
    Default_Background_Data = Default_Background.objects.all()
    Cars_Data = CARS.objects.all()
    Cars_Data= Paginator(Cars_Data, 6)
    page = request.GET.get('page')
    products = Cars_Data.get_page(page)
    totalpages = [x+1 for x in range(Cars_Data.num_pages)]
    Background_Video_Data = Background_Video.objects.all()
    Blog_Data = Blog.objects.all()
    Data= {
        "default_background":Default_Background_Data,
        "cars_Section": products,
        "total_Pages": totalpages,
        "Background_Video":Background_Video_Data,
        "Latest_Blog": Blog_Data,
    }
    return render(request, 'Our_Cars.html', Data) 




def Car_detailPage(request, id):
    Default_Background_Data = Default_Background.objects.all()
    Cars_Data = CARS.objects.all()
    Car_1 = CARS.objects.get(id__exact=id)
    Data = {
        "default_background":Default_Background_Data,
        "Car_Data": Cars_Data,
        "One_Car": Car_1,
        "current_id": int(id)
    }
    return render(request, 'Car_Details.html', Data) 


def reservationPage(request, id):
    Cars_Data = CARS.objects.all()
    Cars_Data= Paginator(Cars_Data, 6)
    page = request.GET.get('page')
    products = Cars_Data.get_page(page)
    Car_1 = CARS.objects.get(id__exact=id)
    Data = {
        "cars_Section": products,
        "One_Car": Car_1,
        "current_id_2": int(id)
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
    cart = request.session.get('cart', {})
    subtotal = sum(float(item['price']) * item['quantity'] for item in cart.values())
    
    rental_days = 1 # Default value
    if request.method == 'POST':
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        if pickup_date and return_date:
            pickup_date = datetime.strptime(pickup_date, '%Y-%m-%d')
            return_date = datetime.strptime(return_date, '%Y-%m-%d')
            rental_days = (return_date - pickup_date).days
    
    context = {
        'subtotal': subtotal,
        'rental_days': rental_days,
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

        return redirect('process_checkout')

    return redirect('checkout')






# def checkout_session(request):
#     try:
#         # Example: base amount before tax
#         base_amount = 1000  # 1000 PKR
#         tax_rate = 0.10     # 10% tax rate

#         # Calculating the final amount with tax
#         aftertax = base_amount + (base_amount * tax_rate)

#         # Creating the Stripe checkout session
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[{
#                 'price_data': {
#                     'currency': 'pkr',
#                     'product_data': {
#                         'name': 'Total Amount',
#                     },
#                     'unit_amount': int(aftertax * 100),  # Stripe expects paisa, hence * 100
#                 },
#                 'quantity': 1,
#             }],
#             mode='payment',
#             success_url='http://127.0.0.1:8000/success/',
#             cancel_url='http://127.0.0.1:8000/cancel/',
#         )
#         # Returning the session ID as JSON
#         return JsonResponse({
#             'sessionId': checkout_session.id
#         })
#     except Exception as e:
#         return JsonResponse({
#             'error': str(e)
#         })





# def checkout_session(request):  
    stripe.api_key = settings.STRIPE_SECRET_KEY
    base_amount = 1000
    tax_rate = 0.10
    aftertax = base_amount + (base_amount * tax_rate)
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'pkr',
                    'product_data': {
                        'name': 'Total Amount ',
                    },
                    'unit_amount': int(aftertax* 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success',
            cancel_url='http://127.0.0.1:8000/cancel',

        )
        if checkout_session:
            order = Orders.objects.create(
                user = request.user,
                amount = checkout_session.amount_total,
                payment_intent = checkout_session.payment_intent,

            )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


def checkout_session(request, order_id):
    # Get the order object
    order = get_object_or_404(Order, id=order_id)

    try:
        # Create the Stripe Checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'pkr',  # Pakistani Rupee
                    'product_data': {
                        'name': f'Order {order.id}',
                    },
                    'unit_amount': int(order.amount * 100),  # Convert to paisa
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f'http://127.0.0.1:8000/success/?session_id={{CHECKOUT_SESSION_ID}}',
            cancel_url=f'http://127.0.0.1:8000/cancel/',
        )

        # Save the Stripe session ID to the order
        order.stripe_session_id = checkout_session.id
        order.save()

        # Redirect the user to the Stripe checkout page
        return redirect(checkout_session.url)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



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
    Default_Background_Data = Default_Background.objects.all()
    General_Questions_Data = General_Questions.objects.all()
    Data={
        "default_background":Default_Background_Data,
        "General_Questions" : General_Questions_Data   
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
    Default_Background_Data = Default_Background.objects.all()
    Team_Cards = Our_Team.objects.all()
    Background_Video_Data = Background_Video.objects.all()
    Testimonial_Data = Testimonial.objects.all()
    Data={
        "default_background":Default_Background_Data,
        "Team_Cards_Data":Team_Cards,
        "Background_Video":Background_Video_Data,
        "Testimonial": Testimonial_Data
    }
    return render(request, 'Our_Team.html',Data) 


def blogPage(request):
    Default_Background_Data = Default_Background.objects.all()
    Blog_Data = Blog.objects.all()
    Blog_Data= Paginator(Blog_Data, 6)
    page = request.GET.get('page')
    products = Blog_Data.get_page(page)
    totalpages = [x+1 for x in range(Blog_Data.num_pages)]
    Data = {
        "default_background":Default_Background_Data,
        "Blog":products,
        "total_Pages": totalpages,
    }
    return render(request, 'Blog.html',Data) 


def Single_postPage(request, id):
    blog = Blog.objects.get(id__exact=id)
    Data = {
        "One_Blog": blog,
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
    cart = Cart(request)
    bookings_total = 0

    session_values = list(cart.session.values())

    if len(session_values) > 5:
        bookings = session_values[5]
    else:
        bookings = []  
    if bookings:
        for book in bookings:
            bookings_total = bookings_total + int(bookings[book]["quantity"])

    if len(session_values) > 5:
        items = session_values[5]
    else:
        items = []  

    subtotal = 0
    if items:  
        for item in items:
            subtotal = subtotal + int(items[item]['price']) * items[item]['quantity']

    Data = {
        "subtotal": subtotal,
        "bookings": bookings_total
    }

    return render(request, 'Reservation.html', Data)




def successPage(request):
    return render(request, 'Success.html')




def cancelPage(request):
    return render(request, 'Cancel.html')





















def quick_Book(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        car = request.POST.get('car','')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')


        '''if not all([name, car, phone, email]):
            messages.error(request, "Not found. Please fill all fields.")
            return redirect('cancel')'''

        try:
            contact = Quick_Book(
                name=name,
                car=car,
                phone=phone,
                email=email
            )
            contact.save()
            messages.success(request, "Success! Your message has been sent.")
            return redirect('home')

        except Exception as e:
            print(f"Error saving contact: {e}")
            messages.error(request, "An error occurred. Please try again.")
            return redirect('home')
            

    return redirect('home')




    





# def orderStatus(request):
    # Fetch all orders for the logged-in user, including their items
    orders = Orders.objects.filter(user=request.user).prefetch_related('orderitem_set')
    profile_picture = None
    city = None
    country = None
    address = None
    phone_no = None

    if request.user.is_authenticated:
        userdata, created = UserProfile.objects.get_or_create(user=request.user)
        profile_picture = userdata.profile_picture.url if userdata.profile_picture else None
        city = userdata.city if userdata.city else None
        country = userdata.country if userdata.country else None
        address = userdata.address if userdata.address else None
        phone_no = userdata.phone_no if userdata.phone_no else None

    # If no orders exist, render with no_order flag
    if not orders.exists():
        shipping_date = timezone.now() + timedelta(days=7)  # Still calculate the general shipping date for display
        return render(request, 'order_status.html', {
            'no_order': True,
            'shipping_date': shipping_date,
            'profile_picture': profile_picture,
            'city': city,
            'country': country,
            'address': address,
            'phone_no': phone_no
        })

    for order in orders:
        order.expected_delivery = order.created_at + timedelta(days=7)

    return render(request, 'order_status.html', {
        'orders': orders,
        'profile_picture': profile_picture,
        'city': city,
        'country': country,
        'address': address,
        'phone_no': phone_no
    })




class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'payments/order_form.html'
    success_url = '/checkout/'

    def form_valid(self, form):
        self.object = form.save()
        # Create Stripe Checkout Session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'pkr',
                    'product_data': {
                        'name': 'Order Payment',
                    },
                    'unit_amount': int(self.object.amount * 100),  # Convert to paisa
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f'http://127.0.0.1:8000/success/?session_id={{CHECKOUT_SESSION_ID}}',
            cancel_url='http://127.0.0.1:8000/cancel/',
        )
        # Save the Stripe session ID to the order
        self.object.stripe_session_id = checkout_session.id
        self.object.save()
        return redirect(checkout_session.url)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order = Order.objects.get(stripe_session_id=session['id'])
        order.status = 'paid'
        order.save()

    return JsonResponse({'status': 'success'})
