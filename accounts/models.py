from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,  PermissionsMixin
from orders.models import Item

class UserManager(BaseUserManager):
    
    def create_user(self, email, password):
        if not email:
            raise ValueError("user must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        #user.is_staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password = None):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        
        return user
    


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    #date_birthday = models.CharField(max_length=30, blank=True)
    #random = models.CharField(max_length=30, blank=True)
    groups = None
    last_login = None
    user_permissions = None
    is_staff = True
    #user_data = models.ForeignKey('accounts.UserData', related_name="users", null=True, blank=True, on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
       return self.is_admin

    def has_perm(self, perm, obj=None):
       return self.is_admin

    def has_module_perms(self, app_label):
       return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self.is_staff



class UserProxy(models.Model):
    first_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True, default="123456789")
    city = models.CharField(max_length=255, null=True, blank=True,default=None)

    date_birthday = models.DateField(null=True, blank=True)
    first_step = models.BooleanField(default=True)
    first_order = models.BooleanField(default=True)
   
    regulations = models.BooleanField(default=False)
    regulations_id = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)
    active_sub = models.BooleanField(default=False)
    id_sub = models.DecimalField(max_digits=7,decimal_places=0,blank=True, null=True)

    price_base = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    
    
    #last_name = models.CharField(max_length=15, null=True, blank=True, default="")
    

    def __str__(self):
        return self.email
    
    #orders = Order.objects.all()
    #items = Item.objects.all()
    #print(items)
    #item_list = models.CharField(choices=items.query, max_length=255)
    def __int__(self):
        return self.email