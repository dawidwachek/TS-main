from django.contrib import admin

from .models import Order,Item

#class ItemInLine(admin.TabularInline):
    #model = Item

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'email_adress','order_status','name_coupon', 'pay_price','item_order']
    readonly_fields = ("order_id","created_at", "updated_at")
    #inlines = [ItemInLine,]
    fieldsets = [
        ('Orders data', {
            'fields':('order_status', 'order_id', 'created_at', 'questionnaire_id')
        }),
        ('Customer data', {
            'fields':('email_adress', 'language','user_name')
        }),
        ('Price data', {
            'fields':('original_price', 'name_coupon', 'pay_price')
        }),
        ('Edit data', {
            'fields':('updated_at', 'editor_email', 'visible')
        }),

    ]
    list_filter = ['order_status','visible']
    search_fields = ['email_adress', 'order_id', 'name_coupon']
    
    #class Meta:
        #model=Order



    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id','email_adress','item_status']

