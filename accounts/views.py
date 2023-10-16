from django.shortcuts import render, redirect
from .models import UserProxy, UserManager, User
from orders.models import Order
from django.contrib.auth import authenticate, login as logfun, logout
from scripts.bot import NewUserBot
from settings.models import Price
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def page_logout(request):
    #empty logout page and return login view
    logout(request)
    return redirect('/accounts/login',{})

def accounts(request):
    #return login site if user link ../accounts/
    return redirect('/accounts/login',{})

def login(request):
    if request.user.is_authenticated:
        return redirect('/accounts/profile', {})
    else:
        if request.method == "POST":
            #getting informations from view
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request,email=email, password=password)

            

            #checking login form
            if email is "":
                error = "empty adress e-mail"
                return render(request, 'login.html',{'error': error})
            if password is "" :
                error = "empty password"
                return render(request, 'login.html',{'error': error})
            if len(password) <= 6:
                error = "password is minimum 7 characters"
                return render(request, 'login.html',{'error': error})
            if not user:
                error = "wrong e-mail or password"
                return render(request, 'login.html',{'error': error})
            
            if User.objects.filter(email__iexact=email).exists():
        
                #login user
                logfun(request, user)
                
                #check user proxy
                obj = UserProxy.objects.filter(email=email)
                if not obj:
                    #return user proxy add informations
                    return redirect('register_more_info')       

                #check first questionnaire
                value = UserProxy.objects.get(email = request.user.email).first_step
                if value:
                    #return first questionnaire site
                    return redirect('/questionnaire', {})
                else:
                    #return profile view
                    return redirect('/accounts/profile', {})
            
            
    return render(request, 'login.html',{})




def register(request):

    #waiting for button click
    if request.method == "POST":

        #getting data from view
        email = request.POST.get("email")
        password = request.POST.get("password")
        check_regulations = request.POST.get("check_regulations")        
        

        #checking register form
        if email is "":
            error = "empty adress e-mail"
            return render(request, 'register.html',{'error': error})
          
        if User.objects.filter(email__iexact=email).exists():
            error = "e-mail is used"
            return render(request, 'register.html',{'error': error})
        
        if password is "" :
            error = "empty password"
            return render(request, 'register.html',{'error': error})
        
        if len(password) <= 6:
            error = "password is minimum 7 characters"
            return render(request, 'register.html',{'error': error})
        
        if check_regulations is None:
            error = "regulations not accepted"
            return render(request,'register.html',{'error': error})
        
        
        
        
        
        #checking user is in user proxy
        obj = UserProxy.objects.filter(email=email)
        if not obj:
            #if empty User proxy go to add informations

            #register account
            User.objects.create_user(email=email, password=password)

            
            
    
            #login to account
            user = authenticate(request,email=email, password=password)
            logfun(request, user)


            #NewUserBot(user_email=email, user_id="", user_name="")

            #go to add more information about client 
            return redirect('register_more_info')

        else:
            #! here start working
            return redirect('error')
            #pass #not empty
            #! here stop working

    #checking user auth and if is auth then go to profile
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return render(request, 'register.html',{})

    


    
@login_required(redirect_field_name="login")
def profile(request):
    #user_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
    #print(str(user_ip))

    obj = UserProxy.objects.filter(email=request.user.email)
    if not obj:
        return redirect('register_more_info')   
    else:
        user_proxy = UserProxy.objects.get(email = request.user.email)
        orders = Order.objects.filter(email_adress = request.user.email).filter(visible = True)
        return render(request, 'profile.html',{"user_proxy": user_proxy, "orders": orders})
    
    
    #getting user orders to view
    
    

@login_required(redirect_field_name="login")
def register_more(request):

    if request.method == "POST":
        #getting data from html
        date_birthday = request.POST.get("date")
        phone_number = request.POST.get("phone")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        city = request.POST.get("city")

        #getting last price from setting
        price_base = Price.objects.filter(is_active = True).filter(valid_at__lte = timezone.now()).last()
        print(str(price_base.price))


        add_user_proxy = UserProxy(email = request.user.email, first_name=first_name, date_birthday = date_birthday ,phone_number = phone_number, last_name=last_name, city=city)
        add_user_proxy.save()
        value = UserProxy.objects.get(email = request.user.email).first_step
        if value:
            return redirect('/questionnaire', {})
        else:
            return redirect('/accounts/profile', {})


        #NewUserBot(user_email=request.user.email, user_id=add_user_proxy.pk, user_name="empty")


    return render(request, 'register_more.html',{})