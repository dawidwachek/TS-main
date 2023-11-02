from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,  PermissionsMixin
from django.contrib.auth.models import Permission
from orders.models import Item
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
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
        user.has_perm()
        
        return user
    
class Permissions(Permission):
    class Meta:
        permissions = [
            ("can_do_something", "Can do something special"),
            # Dodaj inne uprawnienia
        ]
        


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    groups = None
    last_login = None
    #user_permissions = None
    #user_permissions = models.ManyToManyField(Permission, blank=True, default=None)
    user_permissions = models.ManyToManyField(
        verbose_name=_('user permissions'),
        blank=True,
        related_name='user_set',
        related_query_name='user',to='auth.permission',
    )
    

    #perm = models.ManyToManyField(Permission, blank=True, default=None)
    
    is_staff = True
    #user_data = models.ForeignKey('accounts.UserData', related_name="users", null=True, blank=True, on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_superuser(self):
        
        return self.is_superadmin

    @property
    def is_staff(self):
       return self.is_admin

    def has_perm(self, perm, obj=None):
        #print("perm: " + str(self.get_user_permissions))
        if self.is_superuser:
            return self.is_admin
        else:
            return self.is_admin
            #return self.user_permissions.filter(codename=perm).exists()
        
    

    def custom_perm(self):
        print('cust perm: '+ str(self.user_permissions))
        return self.user_permissions
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