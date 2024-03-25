from core.models import SurveyAnswerItem, Answer ,AnswerGoal, AnswerExclusion, ResultItem, AnswerItem, Question, Questionnaire
from orders.models import Order, OrderResultItem, SurveyResult, SurveyResultItem, ItemOrder, OrderResult
import random
from constance import config

#1.Get orders to Personalize - return survey and order          GetOrderStatusAndPersonalize
#2.Get Results from Answers and return to Survey result         PersonalizePPR
#3.Get results from last Orders Results
#   Get last orders with this products
#   Get results form this orders
#4. 2.-3.
#5.Random results from 4

#TODO: change name name 
#TODO: change name class 



def GetOrderStatusAndPersonalize(type_to_personalize):
    #getting all order with paymant accepted status
    #for this order create Survey Answers
    print('start personalize ... ')
    order_payment_succesful = Order.objects.filter(order_status = "PA").all()
    for o in order_payment_succesful:

        item_order = ItemOrder.objects.filter(order = o).last()
        type = item_order.product.product_type
        if type == type_to_personalize:
            survey = item_order.survey
            PersonalizePPR(survey=survey, order=o)
        






def PersonalizePPR(survey, order):
    
    

    #get ???????
    survey_result = SurveyResult.objects.filter(survey=survey).last()
    survey_ans =[]
    
    #get answers for survey
    #for answer append goal
    answers = SurveyAnswerItem.objects.filter(survey=survey).all()
    for a in answers:
        #get answer
        
        ans = AnswerItem.objects.filter(answer=a.answer).last()
        que = Question.objects.filter(name=ans).last()

        result_item = AnswerGoal.objects.filter(answer=a.answer)
        
        for r in result_item:
            #get result and append to survey_ans
            survey_ans.append(r.result_item.slug)
            

    #clear duplicate in survey result answers
    survey_ans = list(dict.fromkeys(survey_ans))


    #get answers for survey
    #for answer remove exclusions 
    answers = SurveyAnswerItem.objects.filter(survey=survey).all()
    for a in answers:
        result_item = AnswerExclusion.objects.filter(answer=a.answer)

        for r in result_item:

            if r.result_item.slug != None:
                #pass
                try: 
                    survey_ans.remove(r.result_item.slug)
                except:
                    pass
            
    

    #add result_item to SurveyResult (create SurveyAnswerItem)
    
    for s in survey_ans:
        result_item = ResultItem.objects.filter(slug=s).last()
        survey_answer_result = SurveyResultItem.objects.create(survey=survey_result, result_item=result_item)

    CreateOrderResultPPR(survey=survey, survey_result=survey_result, order=order)



        

def CreateOrderResultPPR(survey, order, survey_result):

    #TODO: create Order Result

    print('start creating result for order: ', str(survey), ', order: ', str(order))
    print('survey: ', str(survey), ', order: ', str(order), 'survey_result: ', str(survey_result))

    

    #get user for order
    user = Order.objects.get(order_id=order)
    #get order_item for order with product
    order_item = ItemOrder.objects.filter(order=order).last()


    #update ItemOrder at survey_result
    

    #!!OrderResult - 3 ResultItem
    #!!OrderResultItem    Item for OrderResult


    #this now not used
    
    #
    list_survey_result = [] #get results from survey  #DONE

    #last_order_result = [] #get results items from last orders
    
    #available_result_items = [] #survey_result_items - last_result_items

    survey_result_items = SurveyResultItem.objects.filter(survey=survey_result).all()
    
    #get survey results from this survey and add to list
    for s in survey_result_items:
        #print('s: ', str(s.result_item))
        list_survey_result.append(s.result_item.slug)

    
    #clear duplicate in survey result answers
    list_survey_result = list(dict.fromkeys(list_survey_result))


    #TODO: change last 3 survey to get from Product 

    #get user orders with status Order Sended
    last_orders_id = Order.objects.filter(email_adress=user.email_adress).filter(order_status="OS").all()

    #get item orders with product who is calculate
    last_products = ItemOrder.objects.filter(product=order_item.product).all()

    #get item orders with product and status Order Sended
    last_item_orders = last_products.filter(order__in=last_orders_id).all().order_by('-order_id')[:order_item.product.products_to_include]

    #get result items for last items order
    #save to 


    #TODO: get resultsItems from last_products_surveys
    #get last Item order from product and user survey
    print("past add: ",str(list_survey_result))


    for l in last_item_orders:

        result_order_result = OrderResultItem.objects.filter(order_result=l.order_result).all()
        for r in result_order_result:
            
            try:
                list_survey_result.remove(r.result_item.slug)
            except:
                pass
        

    #TODO: add this items to last_result_items
    print("past extend: ",str(list_survey_result))


       
    #create_order_result_item = OrderResultItem.objects.create(order_result=create_order_result)
    #create_order_result_item = OrderResultItem.objects.create(order_result=create_order_result, result_item=last_result_items)

    #TODO: extend last_result_items from survey_result

    #check length result list
    #TODO: change 3 value to get from Product
    if len(list_survey_result) < 3:
        error = 'the result length is too short'
        update_order = Order.objects.filter(order_id=order).update(order_error=error, order_status="PRE")
        print('order: ', str(order), 'error',error)
    else: 
        product_items = order_item.product.product_items
        print('prod_items: ', str(product_items))

        i = 0
        order_result = OrderResult.objects.create(survey=survey)
        while i < product_items:
        #get_randrom from available_result_items
            update_item_order = ItemOrder.objects.filter(order=order).update(survey_result=survey_result, order_result=order_result)
            select_result = random.choice(list_survey_result)
            print('selected: ', str(select_result))
            try:
                list_survey_result.remove(select_result)
                result_item = ResultItem.objects.filter(slug=select_result).last()
                print('res_item: ', str(result_item))
                print('order_result: ', str(order_result))
                create_order_result = OrderResultItem.objects.create(order_result=order_result, result_item=result_item)
            except:
                pass
            print('list survey_result', str(list_survey_result))

            print(str(i+1))
            i+=1
        create_result = ""
        #change order status to Waiting For Acceept
        order = Order.objects.filter(order_id = order)

        
        #!!change status, DON'T DELATE:
        order.update(order_error="", order_status=config.CHANGE_STATUS_IN_MIXER)







        #TODO: add item result to this order and delate from survey_result, 3 time
        #TODO: change status to verified




    #get SurveyAnswerItems

    #get last ResultItems
    #!! this value: is value who is max last orders to get in personalize - use later
    


    #create_order_result_item = OrderResultItem(OrderResult=create_order_result)

    
    