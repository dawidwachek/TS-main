from django.forms import ModelForm
from .models import Questionnaire
from django.contrib.auth.models import User
from django import forms

class CreateQuestionnaireForm(ModelForm):
    class Meta:
        model = Questionnaire
        #fields = '__all__'
        fields = [ 'weigh', 'injury', 'often_injury', 'training','often_training']



class QuestionnaireBasicForm(ModelForm):
    class Meta:
        model = Questionnaire
        
        #model.user_email = 
        fields = [ 'weigh', 'injury', 'training']

class QuestionnaireInjuryForm(ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['often_injury']
  
class QuestionnaireTrainingForm(ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['often_injury']