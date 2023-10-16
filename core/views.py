from django.shortcuts import render, redirect
from django.test import Client
from .models import Questionnaire
from settings.models import Regulation
from .forms import CreateQuestionnaireForm
from orders.forms import OrderForm
from accounts.models import UserProxy
from orders.models import Order
from scripts.bot import QuestionnaireBot, OrderBot

def home(request):
    return render(request, 'home.html',{})

def questionnaire(request):
    
    if request.user.is_authenticated:
        if request.method == "POST":
            return redirect('questionnaire_basic') 

                
        else:
            form = CreateQuestionnaireForm()

        context = {'form' : form}
        return render(request, 'questionnaire.html', context)
    else: 
        return redirect('accounts/login')
    
    

def questionnaire_basic(request):
    
    if request.user.is_authenticated:
        if request.method == "POST":

            #creating questionnaire
            form = CreateQuestionnaireForm(request.POST)
            task = form.save(commit=False)
            task.user_email = request.user.email
            task.save()
            #email = UserProxy.objects.get(email = ).first_step
            obj = UserProxy.objects.filter(email = request.user.email)
            obj.update(first_step = False)
            
            questionnaire_id = task.pk
            user_name = UserProxy.objects.get(email = request.user.email).first_name
            price=UserProxy.objects.get(email = request.user.email).price_base
            #creating order
            order = Order(email_adress = request.user.email, original_price=price, pay_price =price, user_name=user_name, questionnaire_id=questionnaire_id)
            order.save()

            
            
            #here i can get id new order
            o_id = order.pk

            #bot discord
            QuestionnaireBot(questionnaire_id=questionnaire_id, user_email=request.user.email)
            
            #print("order id"+str(o_id))
            request.session['o_id']=o_id
            
            
            
            return redirect('payment', o_id) 
        else:
            form = CreateQuestionnaireForm()

        context = {'form' : form}

        return render(request, 'questionnaire_basic.html', context)
    else: 
        return redirect('accounts/login')
    
    
def questionnaire_injury(request):
    
    #que = request.session.get('que', None)

    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateQuestionnaireForm(request.POST)
            form.save()
        else:
            form = CreateQuestionnaireForm()
        context = {'form' : form}
        return render(request, 'questionnaire_injury.html', context)
    else: 
        return redirect('accounts/login')


def hello(request):
    return render(request, 'hello.html', {})


def faq(request):
    return render(request, 'faq.html', {})
def contact(request):
    return render(request, 'contact.html', {})

def error(request):
    return render(request, 'error_page.html', {})


def regulations(request):
    test = Regulation.objects.filter(is_active = False).last()
    regulation = Regulation.objects.filter(is_active = True).filter(type_regulations="WEB").last().text_regulations
    return render(request, 'regulations.html', {"regulation": regulation})

def marketing_regulations(request):
    regulation = Regulation.objects.filter(is_active = True).filter(type_regulations="MARK").last().text_regulations
    return render(request, 'regulations.html', {"regulation": regulation})

def error404(request, exception):
    return render(request, 'home.html', status=404)