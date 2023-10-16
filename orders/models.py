from django.db import models
from core.models import Questionnaire

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    email_adress = models.EmailField(max_length=255)
    item_status = models.CharField(choices=[
        ('IC', 'Item Created'),
        ('IW', 'Item Verified'),
    ], default="IC", max_length=255)
    editor_email = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.CharField(choices=[
        ("PL", "Polish"),
        ("EN", "English"),
    ], default="EN", max_length=255)

    def __int__(self):
        #return self.item_id
        return self.item_id
    
    
    class Meta:
        ordering = ('item_id',)

    
    
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
    user_name = models.CharField(max_length=30, blank=True)
    language = models.CharField(choices=[
        ("PL", "Polish"),
        ("EN", "English"),
    ], default="EN", max_length=255)
    name_coupon = models.CharField(max_length=15, null=True, blank=True)
    original_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    pay_price = models.DecimalField(max_digits=7, decimal_places=2)
    editor_email = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_order = models.ForeignKey('orders.Item', related_name="items", null=True, blank=True, on_delete=models.CASCADE)
    questionnaire_id = models.CharField(max_length=15, null=True, blank=True)
    visible = models.BooleanField(default=True)
    
    #questionnaire_id = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="questionnaire", null=True, blank=True)
    #test = models.ManyToManyField(Item, null=True, blank=True)
    

    def __int__(self):
        return self.order_id






    

    
