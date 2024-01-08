from django.contrib import admin

from .models import Order, Subscription, SurveyResult, SurveyResultItem, ItemOrder, OrderResult, OrderResultItem


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    extra = 0

@admin.register(ItemOrder)
class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ['id','order', 'product', 'survey', 'survey_result']


class SurveyResultItemInLine(admin.TabularInline):
    model = SurveyResultItem
    extra = 0

@admin.register(SurveyResultItem)
class SurveyResultItemAdmin(admin.ModelAdmin):
    list_display = ['survey', 'result_item']

@admin.register(SurveyResult)
class SurveyResultAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [SurveyResultItemInLine]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'email_adress','order_status','name_coupon', 'pay_price']
    readonly_fields = ("order_id","created_at", "updated_at")
    list_filter = ['order_status','visible']
    search_fields = ['email_adress', 'order_id', 'name_coupon']
    inlines = [ItemOrderInline]
    



@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['sub_id', 'user']
    readonly_fields = ['sub_id']

class OrderResultItemAdmin(admin.ModelAdmin):
    list_display = ['order_result', 'result_item']    

class OrderResultItemInline(admin.TabularInline):
    model = OrderResultItem
    extra = 0

@admin.register(OrderResult)
class OrderResultAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderResultItemInline]