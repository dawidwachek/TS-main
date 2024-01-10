from core.models import SurveyAnswerItem, Answer ,AnswerGoal
from orders.models import Order, OrderResultItem, SurveyResult, SurveyResultItem

def Personalize(survey):
    print('survey: ', str(survey))
    answers = SurveyAnswerItem.objects.filter(survey=survey).all()
    survey_result = SurveyResult.objects.filter(survey=survey).last()
    #order = Order.objects.filter(questionnaire_id = survey).last()
    #print('order: ', str(order))
    print('answers: ', str(answers))

    #adding result items to SurveyResultItem???
    for a in answers:
        #answer = Answer.objects.filter(answer = a.answer.answer).all()
       # print('ans: ', str(a))
        result_item = AnswerGoal.objects.filter(answer=a.answer)
        for r in result_item:

            add_survey_result_item = SurveyResultItem.objects.create(survey=survey_result, result_item=r.result_item)
            print('add to survey result: ', str(add_survey_result_item))



    #for a in answers:


        #oal = AnswerGoal.objects.filter(answer=answer)
        #print("goal: ", str(goal))

        #goal = AnswerGoal.objects.filter(answers=a.answer).all()
        #print("goal: ", str(goal))





        #TODO:
        #add Goal ResultItem to SurveyResultItem

        #delate Exclusions ResultItem from SurveyResultItem
    