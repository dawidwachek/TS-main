from django.contrib import admin
from django.http.request import HttpRequest
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required


from .models import User, UserProxy, CustomerAdress


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    print('self:')

    list_display = ['email', 'is_admin', 'is_superuser', 'is_staff']
    fieldsets = [
        ('User general data', {
            'fields':('email', 'password')
        }),
        ('Permissions', {
            'fields':('is_admin','is_active','is_superadmin', 'user_permissions')
        })
        ]
    filter_horizontal = ('user_permissions',)
    


@admin.register(UserProxy)
class UserProxyAdmin(admin.ModelAdmin):

    

    list_display = ['email','first_name', 'active_sub','first_step', 'first_order']
    fieldsets = [
        ('Contact', {
            'fields':('email', 'phone_number')
            }
        ),

        ('User', {
            'fields':('first_name', 'last_name', 'date_birthday')
            }
        ),
        
        ('Survey data', {
            'fields':( 'first_step', 'first_order')
            }
        ),
        ('Consents data', {
            'fields':('regulations', 'regulations_id', 'active_sub', 'id_sub')
            }
        ),
        ('Price data', {
            'fields':('price_base',)
            }
        ),
        
        ]
    
    
@admin.register(CustomerAdress)
class CustomerAdressAdmin(admin.ModelAdmin):
    # = ['user', 'city']
    list_display = ['user', 'city', 'adress_type']
    fieldsets = [
        ('None',{
            'fields':('user','adress_type',)
        }),
        ('Adress', {
            'fields':('adress_line_1', 'adress_line_2', 'post_code', 'city', 'country')
            }

        ),
    ]
    