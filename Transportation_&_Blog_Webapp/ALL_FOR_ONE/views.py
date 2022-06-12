from random import choices
from django.shortcuts import redirect, render
from django.contrib import messages
from ALL_FOR_ONE.models import SignUp, Blog, Comments, Contact
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from ALL_FOR_ONE import database
import razorpay
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    # if request.method == 'POST':
    #     location = request.POST.get('Location')
    #     destination = request.POST.get('destination')
    #     d_time = request.POST.get('d_time')
    #     search = Search(yourlocation=location, destination=destination, d_time=d_time)
    #     search.save()
    #     messages.info(request, 'Searching, data is being fetched!')
    if request.session.has_key('is_login'):
        return render(request, 'index.html',{'Name': request.session['Name']})
    else:
        return render(request, 'index.html')

def Data(request):
    TrainNum = request.POST['TrainNum']
    Destination = request.POST['Destination']
    Deptime = request.POST['Deptime']
    data = database.Data['Trains']
    for i in data:
        if i['Number'] == TrainNum and i['Destination'] == Destination :# and i['ScheduleDeparture'] == Deptime:
            return render(request, 'Show.html', {'data': i})

def Trains(request):
    data = database.Data['Trains']
    return render(request, 'trains.html', {'data':data})

def About(request):
    if request.session.has_key('is_login'):
        return render(request, 'About.html',{'Name': request.session['Name']})
    else:
        return render(request, 'About.html')    
    
def blog(request):
    if request.session.has_key('is_login'):
        blog = Blog.objects.all().order_by('-id')
        data = Comments.objects.all()
        return render(request, 'blog.html', {'Name': request.session['Name'], 'Blog':blog, 'comments':data})
    else:
        blog = Blog.objects.all().order_by('-id')
        data = Comments.objects.all()
        return render(request, 'blog.html', {'Blog':blog, 'comments':data})

def AddBlog(request):
    if request.method=='POST':
        # U_id = request.session['Name']
        File = request.FILES['File']
        Title = request.POST.get('Title')
        Detail = request.POST.get('Desc')
        U_Name = request.POST.get('Publisher')
        BLOG = Blog(File=File, Title=Title, Detail=Detail, U_Name=U_Name)
        BLOG.U_id_id=request.session['Data']
        BLOG.save()
        messages.success(request, ' Your Blog added successfully')
        return redirect('/blog')
    return render(request, 'AddBlog.html', {'Name': request.session['Name']})

def comments(request):
    comment = request.POST['comment']
    comments = Comments(comment=comment)
    comments.Blog_id_id = request.POST['blog_id']
    comments.U_id_id = request.session['Data']
    comments.save()
    return redirect('/blog')

def Contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your Response has been recorded!')
    if request.session.has_key('is_login'):
        return render(request, 'Contact.html',{'Name': request.session['Name']})
    else:
        return render(request, 'Contact.html')

def Signup(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Phone = request.POST.get('Phone')
        Address = request.POST.get('Address')
        check = SignUp.objects.filter(Email=Email).count()
        if check == 0 :
            Signup = SignUp(Name=Name, Email=Email, Password=Password, Phone=Phone, Address=Address)
            Signup.save()
            messages.success(request, 'Registration has been succesfully done')
            subject = 'Registration done successfully'
            message = ' thank you for register '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [Email]   
            send_mail(subject, message, email_from, recipient_list)
            return redirect('Login')
        else :
            messages.error(request, 'This Email is already registered')
            return redirect('Signup')
    return render(request, 'Signup.html')

def Login(request):
    # login session check
    if request.session.has_key('is_login'):
        return redirect('/')
    # login details check
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        check = SignUp.objects.filter(Email=Email, Password=Password).count()
        if check > 0 :
            request.session['is_login'] = True
            messages.success(request, 'Login successfully')
            # getting user data after login, for displaying at navbar
            data = SignUp.objects.get(Email=Email)
            request.session['Name'] = data.Name
            request.session['Data'] = data.id
            return render(request, 'index.html') 
        else:
            messages.error(request, 'Wrong username or password!!!')
            return redirect('Login')
    return render(request, 'Login.html')

def Forgotpass(request):
    if request.method == 'POST':
        # getting user input data
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        # confirming user data from DB 
        check= SignUp.objects.filter(Email=Email).count()
        if check > 0:
            data = SignUp.objects.get(Email=Email)
            # putting data to DB data that we get above
            data.Password=Password
            data.save()
            messages.success(request, 'Password changed successfully')
            return redirect('Login')  
        else:
            messages.error(request, 'Somthing went wrong!!!')
            return redirect(request, 'Forgotpass')
    return render(request, 'Forgot.html')

def Logout(request):
    if request.session.has_key('is_login'):
        del request.session['is_login']
        messages.info(request, 'LOG OUT successfully')
        return redirect('Login')
    else:
        messages.error(request, 'Login First!!!')
        return render(request, "index.html")

def User(request):
    Data = SignUp.objects.get(id=request.session['Data'])
    return render(request, 'Userdata.html',{'Name':request.session['Name'], 'Data': Data})

def Edit(request):
    if request.method == 'POST':
        data=SignUp.objects.get(id=request.session['Data'])
        data.Name = request.POST.get('Name')
        data.Email = request.POST.get('Email')
        data.Password = request.POST.get('Password')
        data.Phone = request.POST.get('Phone')
        data.Address = request.POST.get('Address')
        if request.POST.get('Pro_Img'):
            data.Pro_Img = request.FILES('Pro_Img')
        check = SignUp.objects.filter(id=request.session['Data']).count()
        if check == 1 :
            data.save()
            messages.success(request, 'Data has been succesfully Updated')
            return redirect('User')
        else :
            messages.error(request, 'This Email is already registered')
            return redirect('User')


# payment
@csrf_exempt
def payment(request):
    if request.method == "POST":
        email = request.POST['subEmail']
        subject = 'Thank you for subscribe to our site'
        message = ' it means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]   
        send_mail(subject, message, email_from, recipient_list)

        amount = float(str(request.POST.get('amount'))) * 100

        # create Razorpay client
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))

        # create order
        response_payment = client.order.create(dict(amount=amount, currency='INR'))
        return render(request, 'payment.html', {'payment': response_payment})


@csrf_exempt
def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']                    
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
    
    return redirect('/')