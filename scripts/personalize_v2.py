
from core.models import SurveyAnswerItem
from orders.models import ItemOrder


#get goal from answer and add to list (for category)
#cleare duplicate
#get exclusion from answer and remove from list
#get latest items for user and results (price date/time, payment_accepted and next status)
#remove latest results items

def Personalize(order_id):
    #get order data to personalize
    print('personalization order: ', order_id)

    #get order items
    item_order = ItemOrder.objects.filter(order = order_id).all()
    for i in item_order:

        #get surveys
        survey = i.survey

        #get answers to survey
        survey_answer_items = SurveyAnswerItem.objects.filter(survey=survey).all()
        for a in survey_answer_items:
            print('test: ' + str(a.answer))
        

        
    #type_item_order = item_order.product.product_type
    #survey_item_order = item_order.survey
        
def GetOrderToPersonalize(order_id):
    pass

def GetSurveyAnswers():
    pass

def GetAnswerGoals():
    pass