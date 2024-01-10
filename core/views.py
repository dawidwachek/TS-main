from django.shortcuts import render, redirect
from django.test import Client
from .models import Questionnaire, AnswerItem, Product, SurveyAnswerItem, Answer, Question
from settings.models import Regulation, QuestionSequence, QuestionItem, Translation as Language
from orders.forms import OrderForm
from accounts.models import UserProxy
from orders.models import Order, ItemOrder, SurveyResult
from scripts.bot import QuestionnaireBot, OrderBot
from scripts.translate import Translation
from scripts.personalize import Personalize

def home(request):
    return render(request, 'home.html',{})

def hello(request):
    return render(request, 'hello.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def error(request):
    return render(request, 'error_page.html', {})


def regulations(request):
    regulation = Regulation.objects.filter(is_active = True).filter(type_regulations="WEB").last().text_regulations
    return render(request, 'regulations.html', {"regulation": regulation})

def marketing_regulations(request):
    regulation = Regulation.objects.filter(is_active = True).filter(type_regulations="MARK").last().text_regulations
    return render(request, 'regulations.html', {"regulation": regulation})

def error404(request, exception):
    return render(request, 'home.html', status=404)

def survey(request, product_tag ,slug):

    #get questionnaire slug id to upadte
    slug_id = slug


    #get last active questionnaire sequence to show
    product = Product.objects.filter(tag=product_tag).last()
    product_id = product.id
    questions_sequence = QuestionSequence.objects.filter(is_active = True).filter(product = product_id).last()
    questions_sequence_len = questions_sequence.lenQuestionSequenc()
    
    #get items survey
    questionsitems = QuestionItem.objects.filter(question_sequence = questions_sequence)
   
    #get anwers
    answers = AnswerItem.objects.all()

    
    #create questionnaire
    if request.method == "POST":

        survey_id = Questionnaire.objects.filter(slug=slug).last()

        for que in questionsitems:
            
            answer = request.POST.get(str(que))
            if answer != None:

                survey_question = Question.objects.filter(name = que.question).last()
                survey_answer = Answer.objects.filter(name = answer).last()
                

                surwey_answer_item = SurveyAnswerItem.objects.create(question = survey_question, answer=survey_answer, survey=survey_id)



        for que in answers:
            answer = request.POST.get(str(que.answer.answer))
            if answer != None and answer != "":
                #print('test--', str(que), ', ', str(que.answer), ', ', str(answer))
                
                survey_question = Question.objects.filter(name = que).last()
                survey_answer = Answer.objects.filter(name = que.answer.name).last()
                survey_answer_value=''
                if survey_question.question_type == "text":
                    survey_answer_value = answer
                surwey_answer_item = SurveyAnswerItem.objects.create(question = survey_question, answer=survey_answer, survey=survey_id, answer_value=survey_answer_value)

    #####
        #create order            
        order = Order.objects.create(email_adress = request.user.email)
        survey_result = SurveyResult.objects.create(survey=survey_id)
        print('s_r: ', str(survey_result))
        item_order = ItemOrder.objects.create(order = order, survey = survey_id, product = product)
       
        return redirect('payment', order_id=order.order_id)

    context = {
        "questions": questionsitems,
        'answers': answers,
        'survey_len': questions_sequence_len,
    }

    return render(request, 'survey.html', context)


def new_survey(request, product_tag):

    #creating survey for getting slug
    quest = Questionnaire()
    quest.product = Product.objects.filter(tag = product_tag).last()
    quest.save()
    slug = quest.slug

    #set user profile for survey if user is auth
    if request.user.is_authenticated:
        obj = Questionnaire.objects.filter(slug = quest.slug)
        obj.update(user_email = request.user.email)

    return redirect('survey', product_tag, slug)

def product(request, req_product):
    #checking product type to redirect to 
    product = Product.objects.filter(tag = req_product).last()

    #not product
    if not product:
        return redirect('home')
    #checking active product
    if product.is_active == False:
        return redirect('home')
    #Personalized Product Random - random if goal end exclusion
    if product.product_type == 'PPR':
        return redirect('new_survey', str(product.tag))
    #Personalized Product Plus - plus or minus from product items
    if product.product_type == 'PPP':
        return redirect('home')
    #One Product Online - **e-book etc.
    if product.product_type == 'OPO':
        return redirect('home')
    #One Product Phisical - **table etc.
    if product.product_type == 'OPP':
        return render(request, 'product.html')
    #else options
    else:
        return redirect('home')
    #return render(request, 'survey.html')













def test(request):

    if request.method == "POST":
        print("start test")
        survey = Questionnaire.objects.last()
        Personalize(survey=survey)
    test_result = "test text"
    


    return render(request, 'test.html', {'test_result': test_result})