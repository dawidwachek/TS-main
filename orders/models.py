from django.db import models
from core.models import Questionnaire, Product, ResultItem
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

#order
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_status = models.CharField(choices=[
        ("OC", "Order Created"),
        ("WP", "Waiting for Payment"),
        ("PA", "Payment Accepted"),
        ("PE", "Payment Error"),
        ("WA", "Waiting for Acception"),
        ("OA", "Order Accepted"),
        ("OS", "Order Sended"),
    ],default='OC', max_length=255)
    email_adress = models.EmailField(max_length=255)
    #TODO: change user_name to auto complete
    user_name = models.CharField(max_length=30, blank=True)
    #TODO: add language and pair with translations
    language = models.CharField(choices=[
        ("PL", "Polish"),
        ("EN", "English"),
    ], default="EN", max_length=255)
    name_coupon = models.CharField(max_length=15, null=True, blank=True)
    original_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, blank=True, null=True)
    pay_price = models.DecimalField(max_digits=7, decimal_places=2, default=None, blank=True, null=True)
    editor_email = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __int__(self):
        return self.order_id
    def __str__(self):
        return f'#{self.order_id}'

class ItemOrder(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    survey = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    survey_result = models.ForeignKey(SurveyResult, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    




class Subscription(models.Model):
    sub_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    



class OrderResult(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    #user = models.ForeignKey('accounts.User', on_delate=models.DO_NOTHING )
    #Result Item Inline
    
    
class OrderResultItem(models.Model):
    order_result = models.ForeignKey(OrderResult, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)
    result_item = models.ForeignKey(ResultItem, on_delete=models.DO_NOTHING, default=None, blank=True,null=True)