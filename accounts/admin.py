from django.contrib import admin

from .models import User, UserProxy

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_admin']
    fieldsets = [
        ('User general data', {
            'fields':('email', 'password')
        }),
        ('Permissions', {
            'fields':('is_admin','is_active','is_superadmin')
        })
        ]
    

@admin.register(UserProxy)
class UserProxyAdmin(admin.ModelAdmin):
    list_display = ['email','first_name', 'active_sub','first_step', 'first_order']
    fieldsets = [
        ('Base data', {
            'fields':('email','first_name', 'last_name', 'phone_number', 'city')
            }
        ),
        ('survey data', {
            'fields':('date_birthday', 'first_step', 'first_order')
            }
        ),
        ('consents data', {
            'fields':('regulations', 'regulations_id', 'active_sub', 'id_sub')
            }
        ),
        ('price data', {
            'fields':('price_base',)
            }
        ),
        
        ]