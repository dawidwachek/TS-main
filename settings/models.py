from django.db import models
from django.core.exceptions import ValidationError
import sys
from ckeditor.fields import RichTextField
from core.models import Product
from core.models import Question
from core.models import Answer, AnswerItem

def validator_tag(value):
    if ' ' in value:
        raise ValidationError('" " unavailable')
    #if '.' in value:
    #    raise ValidationError('"." unavailable')

# Create your models here.

class Regulation(models.Model):
    regulation_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(choices=[
        ('pl', 'PL'),
        ('en', 'EN')
    ], max_length=5)
    is_active = models.BooleanField(default=False)
    text_regulations = models.TextField(blank=True, null=True)
    type_regulations = models.CharField(choices=[
        ('WEB','website'),
        ('MARK','marketing'),
        ('SUB','subscription'),
        ('ONE','one-off'),
        ('BUY','buy')
    ], max_length=255, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Regulation"

    def __str__(self):
        return f'{self.language + " (" + str(self.regulation_id) + ")"}'




class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(choices=[
        ('PLN', 'PLN'),
        ('GBP', 'GBP'),
        ("EURO", 'EURO'),
    ],default="PL", max_length=5)
    valid_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    price_model = models.CharField(choices=[
        ('ALL', 'Personalized'), #all personalized
        ('BS', 'Business Small'), #manual training 
        ('BB', 'Business Big') #trainer model bussines
    ], max_length=255, default="ALL")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Price"





class ActivityLog(models.Model):
    activity_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    activity_type = models.CharField(choices=[
        ('1','system'),
        ('2','user')
    ], max_length=5)
    text_log = models.TextField(blank=True, null=True)
    user_log = models.EmailField(blank=True, null=True)
    status_log = models.CharField(choices=[
        ('1','start'),
        ('2','end')
    ], max_length=5)

    class Meta:
        verbose_name_plural = "Activity Log"

    



    


class QuestionSequence(models.Model):
    question_sequence_id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None, null=True, blank=True)

    #man = Question.objects.all()


    class Meta:
        verbose_name_plural = "Question Sequence"

    def __str__(self):
        
        return f'{self.product.tag}'

    
    def lenQuestionSequenc(self):
        que = QuestionItem.objects.filter(question_sequence=self.question_sequence_id)
        return len(que)





#view for testing value

class QuestionItem(models.Model):
    sequence = models.AutoField(primary_key=True, default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answer = models.ManyToManyField(Answer, default=None, blank=True)
    question_sequence = models.ForeignKey(QuestionSequence, on_delete=models.CASCADE, default=None)
    min_value = models.CharField(blank=True, null=True, max_length=5, default=0, help_text = 'save this item in QuestionItem to update min value')
    max_value = models.CharField(blank=True, null=True, max_length=5, default=0, help_text = 'save this item in QuestionItem to update max value')

    def save(self, *args, **kwargs):
        mn_value = AnswerItem.objects.filter(question=self.question)
        l = []
        for m in mn_value:
            if m.minimum_value != None:
                l.append(m.minimum_value)
        self.min_value = min(l)

        mx_value = AnswerItem.objects.filter(question=self.question)
        l = []
        for m in mx_value:
            if m.maximum_value != None:
                l.append(m.maximum_value)
        self.max_value = max(l)

        return super().save(*args, **kwargs)

    
    def mx_value(self):
        max_value = AnswerItem.objects.filter(question=self.question)
        l = []
        for m in max_value:
            if m.maximum_value != None:
                l.append(m.maximum_value)
        o = max(l)
        return o

    def __str__(self):
        return f'{self.question}'
    
class Translation(models.Model):
    tag = models.CharField(max_length=255, validators=[validator_tag])
    l_en = models.TextField()
    l_pl = models.TextField(blank=True, null=True, default=None)
    l_de = models.TextField(blank=True, null=True, default=None)
    l_it = models.TextField(blank=True, null=True, default=None)
    #l_cz = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.tag}'

