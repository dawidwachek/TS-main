from django.contrib import admin
from django.http.request import HttpRequest
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required


from .models import User, UserProxy


class ReadOnlyAdminMixin:
    def has_permission(self, request, obj, action):
        opts = self.opts
        code_name = f'{action}_{opts.model_name}'
        if obj:
            return request.user.has_perm(f'{opts.app_label}.{code_name}', obj)
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        
        return True
        #return self.has_permission(request, obj, 'delate')
   
    def has_add_permission(self, request, obj=None):
        if request.user.has_perm('user.add_user'):
            return self.has_permission(request, obj, 'add')
        else:
            return False
        #return self.has_permission(request, obj, 'add')
    
    def has_change_permission(self, request, obj=None):
        return True
    def has_view_permission(self, request, obj=None):
        #print('self: '+ str(self)+ " request: "+ str(request))
        return True
        #return self.has_permission(request, obj, 'view')


#@permission_required('accounts.view_user')
@admin.register(User)
class UserAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    #cust = CustPerm.has_cust_perm(self=)
    #print ('custom: '+ str(cust))
    #def has_add_permission(self, request, obj=None):
        #return ReadOnlyAdminMixin.has_add_permission(self, request=request)
    #def has_permission(self, request, obj, action):
        #print('perm:: '+ str(self)+ " request: " +str(request)+ " obj: " +str(obj) + " action: "+ str(action))



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
    

#admin.site.register(User, UserAdmin)

#@permission_required('accounts.UserProxyAdmin')




@admin.register(UserProxy)
class UserProxyAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):


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