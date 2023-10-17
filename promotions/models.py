from django.db import models

# Create your models here.
class Reflink(models.Model):
    reflink_id = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uses_reflink = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    link_reflink = models.TextField(default="your reflink is domain + reflink/ + id reflink"+"working at this :)")

    def __str__(self):
        #return self.item_id
        return self.name_user

class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_name = models.CharField(unique=True, max_length=255, null=False)
    is_active = models.BooleanField(default=False)
    zero_amount = models.BooleanField(default=False, help_text='coupon resetting the amount')
    created_at = models.DateTimeField(auto_now_add=True)
    uses_coupon = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    max_uses_coupon = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)
    value_coupon = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text='amount or percentage')
    type_coupon = models.CharField(choices=[
        ("PE", "percent"),
        ("AM", "amount"),], null=True , max_length=255)
    assigment = models.BooleanField(default=False)
    email_assignment = models.EmailField(blank=True, default=None, null=True)
    max_value_coupon = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    start_date_use = models.DateField(default=None, blank=True, null=True)
    end_date_use = models.DateField(default=None, blank=True, null=True)

    
    

    def __str__(self):
        
        return self.coupon_name
    

class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=False)
    has_link = models.BooleanField(default=False)
    link = models.CharField(max_length=1000, null=True, default=None)
    text = models.CharField(max_length=255, null=True, default=None)
    start_at = models.DateField(default=None, blank=True, null=True)
    end_at = models.DateField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)