from django.db import models

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


class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(choices=[
        ('PL', 'PLN'),
        ('EN', 'GBP')
    ], max_length=5)
    valid_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    price_model = models.CharField(choices=[
        ('ALL', 'Personalized'), #all personalized
        ('BS', 'Business Small'), #manual training 
        ('BB', 'Business Big') #trainer model bussines
    ], max_length=255, default="ALL")

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