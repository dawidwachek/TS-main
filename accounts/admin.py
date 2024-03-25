from django.contrib import admin
from django.http.request import HttpRequest
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate
from .models import User, UserProxy, CustomerAdress
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import PermissionRequiredMixin

#user = authenticate()
class AdminPermissions:
    def has_delete_permission(self, request, obj=None):
        perm_list = []
        user = request.user
        if user.is_superadmin != True:
            perm_func = user.has_custom_perm()
            for t in perm_func:
                
                codename = t.codename
                app_label = t.content_type.app_label

                t_codename = self.model._meta.model_name
                t_app_label = self.model._meta.app_label
                func = '.delete_'

                perm_list.append(app_label+'.'+codename)
                
            if t_app_label+func+t_codename in perm_list:
                return True
            else:
                return False
            
        else: 
            return True

    def has_add_permission(self, request, obj=None):
        perm_list = []
        user = request.user
        if user.is_superadmin != True:
            perm_func = user.has_custom_perm()
            for t in perm_func:
                codename = t.codename
                t_codename = self.model._meta.model_name
                app_label = t.content_type.app_label
                t_app_label = self.model._meta.app_label
                func = '.add_'

                perm_list.append(app_label+'.'+codename)

            if t_app_label+func+t_codename in perm_list:
                return True
            else:
                return False
        else:
            return True
    def has_view_permission(self, request, obj=None):
        perm_list = []
        user = request.user
        if user.is_superadmin != True:
            perm_func = user.has_custom_perm()
            for t in perm_func:
                codename = t.codename
                t_codename = self.model._meta.model_name
                app_label = t.content_type.app_label
                t_app_label = self.model._meta.app_label
                func = '.view_'
                perm_list.append(app_label+'.'+codename)
            if t_app_label+func+t_codename in perm_list:
                return True
            else:
                return False
        else:
            return True
    def has_change_permission(self, request, obj=None):
        perm_list = []
        user = request.user
        if user.is_superadmin != True:
            perm_func = user.has_custom_perm()
            for t in perm_func:
                codename = t.codename
                t_codename = self.model._meta.model_name
                app_label = t.content_type.app_label
                t_app_label = self.model._meta.app_label
                func = '.change_'
                perm_list.append(app_label+'.'+codename)
            if t_app_label+func+t_codename in perm_list:
                return True
            else:
                return False
        else:
            return True






@admin.register(User)
class UserAdmin(admin.ModelAdmin, AdminPermissions):
    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    

    list_display = ['email', 'is_admin', 'is_staff', 'is_superadmin', 'is_superuser']
    search_fields = ['email']
    fieldsets = [
        ('User general data', {
            'fields':('email', 'password')
        }),
        ('Permissions', {
            'fields':['is_admin','is_active','is_superadmin','is_staff' ,'user_permissions','groups',]
        })
        ]
    filter_horizontal = ['user_permissions','groups',]
    


#@admin.register(UserProxy)
class UserProxyAdmin(admin.ModelAdmin, AdminPermissions):
    
    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    

    

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
class CustomerAdressAdmin(admin.ModelAdmin, AdminPermissions):

    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    
    # = ['user', 'city']
    list_display = ['user', 'city', 'country', 'adress_type']
    fieldsets = [
        ('None',{
            'fields':('user','adress_type',)
        }),
        ('Adress', {
            'fields':('adress_line_1', 'adress_line_2', 'post_code', 'city', 'country')
            }

        ),
    ]
    search_fields = ('user__email',)
    list_filter = ['adress_type']
    