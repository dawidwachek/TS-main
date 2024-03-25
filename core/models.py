from django.db import models
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.views import View

from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string



def validator_tag(value):
    if ' ' in value:
        raise ValidationError('" " unavailable')


#questions
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    question_text = models.CharField(max_length=255, blank=True)
    question_description = models.TextField(default=None, blank=True, null=True)
    question_type = models.CharField(choices=[
        ('text', 'Text - not active now'),
        ('button', 'One choice'),
        ('choice', 'More Choice'),
        ('integer', 'Value'),
        ('category', 'Category Choice'),
    ], default='button', max_length=255, blank=True, null=True)


    def __str__(self):
        return f'{self.name}'
    
    def get_text(self):
        return f'{self.name}'

#answers
class Answer(models.Model):
    name = models.CharField(max_length=100)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name + " - " + self.answer}'
    
#answer for question - connecting
class AnswerItem(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    minimum_value = models.IntegerField(default=None, blank=True, null=True, help_text=">= min")
    maximum_value = models.IntegerField(default=None, blank=True, null=True, help_text="< max")


    def __str__(self):
        return f'{self.question}'
    
class MixerCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default=None, max_length=100)
    def __str__(self):
        return f'{self.name}'

#products
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)

    mixer_category = models.ManyToManyField(MixerCategory, default=None, blank=True)
    #price
    product_type = models.CharField(choices=[
        ('OPP', 'one product phisical'),
        ('OPO', 'one product online'),
        ('PPP', 'personalized product plus'),
        ('PPR', 'personalized product random'),
    ], max_length=100, default='PPR')
    #category_to_include = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    product_items = models.IntegerField(default=3, blank=False, null=False)
    products_to_include = models.IntegerField(default=3, blank=False, null=False, help_text="products to include with exclusion in mixer")

    def __str__(self):
        return f'{self.name}'
    

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=False)
    products = models.ManyToManyField(Product, blank=True, default=None)



#survey
class Questionnaire(models.Model):
    slug = models.CharField(blank=True, null=True, max_length=102)
    questionnaire_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_email = models.EmailField(max_length=100, blank=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    
    def __int__(self):
        return f'questionnaire id: {self.questionnaire_id}'
    
    def __str__(self):
        return f'#{self.questionnaire_id}'
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =  get_random_string(length=40)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Survey"

class ResultCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True, default=None)
    def __str__(self):
        return f'{str(self.id) + " - " + self.name}'
    #len_result = models.IntegerField(default=1,blank=False, null=False)
    
#answers for survey - connecting
class SurveyAnswerItem(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    survey = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, default=None)
    #category_result = models.ForeignKey(ResultCategory, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    answer_value = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.answer}'
    



#result **exercise
class ResultItem(models.Model):
    slug = models.CharField(max_length=100, default=None, blank=True, null=True, help_text="is autocomplete")
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    url = models.URLField(default=None, blank=True, null=True, help_text="link to video")
    category = models.ForeignKey(ResultCategory, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    #image = models.ImageField(default=None, blank=True, null=True, help_text='image')

    def __str__(self):
        return f'{self.name + " - " + self.slug}'

    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug =  get_random_string(length=40)
        if not self.name:
            self.name = self.slug
        return super().save(*args, **kwargs)

#result for answer - connecting but goal for result
class AnswerGoal(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    result_item = models.ForeignKey(ResultItem, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f'{self.answer}'

#result for answer - connecting but exclusion for result
class AnswerExclusion(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    result_item = models.ForeignKey(ResultItem, on_delete=models.CASCADE, default=None)   




class AnswerResultCategoryItem(models.Model):
    result_category = models.ForeignKey(ResultCategory, on_delete=models.CASCADE, default=None)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    len_result = models.IntegerField(default=1, blank=False, null=False)
    def __str__(self):
        return f'{self.result_category}'


class SurveyResultCategoryItem(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE, default=None)
    survey = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, default=None)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    def __str__(self):
    #    pass
        return f'{self.answer}'
