from django.db import models
from core.models import Questionnaire, Product, ResultItem, ResultCategory
from accounts.models import User
from simple_history.models import HistoricalRecords
#from accounts.models import User


#survey result 
class SurveyResult(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    
    def __str__(self):
        return f'{self.id}'

#survey result - connetcting
class SurveyResultItem(models.Model):
    survey = models.ForeignKey(SurveyResult, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    result_item = models.ForeignKey(ResultItem, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    
    def result_category(self):
        return self.result_item.category

#order
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_status = models.CharField(choices=[
        ("OC", "Order Created"),
        ("WP", "Waiting for Payment"),
        ("PA", "Payment Accepted"),
        ("PE", "Payment Error"),
        ("WA", "Waiting for Acception"),
        ('PRE', 'Personalizations Error'),
        ("OA", "Order Accepted"),
        ("OS", "Order Sended"),
        ("OCA", "Order Cancelled"),
        ("OR", "Order Refounded"),
    ],default='OC', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True,null=True)
    #email_adress = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    #TODO: change user_name to auto complete
    user_name = models.CharField(max_length=30, blank=True)
    #TODO: add language and pair with translations
    language = models.CharField(choices=[
        ("PL", "Polish"),
        ("EN", "English"),
    ], default="EN", max_length=255)
    order_error = models.CharField(max_length=255, null=True, blank=True)
    name_coupon = models.CharField(max_length=15, null=True, blank=True)
    original_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, blank=True, null=True)
    pay_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, blank=True, null=True)
    editor_email = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(default=None, blank=True, null=True)
    visible = models.BooleanField(default=True)

    #def user_name(self):
    #    return self.email_adress

    history = HistoricalRecords()

    def __int__(self):
        return self.order_id
    def __str__(self):
        return f'#{self.order_id}'




class Subscription(models.Model):
    sub_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    



class OrderResult(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    #user = models.ForeignKey('accounts.User', on_delate=models.DO_NOTHING )
    #Result Item Inline
    def __str__(self):
        return f'{self.id}'
    
    
class OrderResultItem(models.Model):
    order_result = models.ForeignKey(OrderResult, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    result_category = models.ForeignKey(ResultCategory, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    result_item = models.ForeignKey(ResultItem, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    

class ItemOrder(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    survey = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    survey_result = models.ForeignKey(SurveyResult, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    order_result = models.ForeignKey(OrderResult, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True,null=True)
    

