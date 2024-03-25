from django.contrib import admin
from scripts.personalize import PersonalizePPR
from simple_history.admin import SimpleHistoryAdmin
from .models import Order, Subscription, SurveyResult, SurveyResultItem, ItemOrder, OrderResult, OrderResultItem

@admin.action(description="Change status to Order Sended ")
def change_status_to_order_sended(modeladmin, request, queryset):
    queryset.update(order_status="OS")

@admin.action(description="Change status to Order Cancelled ")
def change_status_to_order_cancelled(modeladmin, request, queryset):
    queryset.update(order_status="OCA")

@admin.action(description="Change visible to False ")
def change_visible_to_false(modeladmin, request, queryset):
    queryset.update(visible = False)

@admin.action(description="Change user to empty")
def change_email_adress_to_empty(modeladmin, request, queryset):
    queryset.update(user="")




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
    readonly_fields = ['result_category']
    list_display = ['survey', 'result_category' ,'result_item',]

@admin.register(SurveyResult)
class SurveyResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'survey']
    inlines = [SurveyResultItemInLine]

class OrderHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["order_id", "user", "order_status"]
    history_list_display = ["order_status"]
    #search_fields = ['name', 'user__username']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user','order_status','name_coupon', 'pay_price']
    readonly_fields = ("order_id","created_at", "updated_at")
    list_filter = ['order_status','visible']
    search_fields = ['user', 'order_id', 'name_coupon']
    autocomplete_fields = ['user']
    inlines = [ItemOrderInline]
    actions = [change_status_to_order_sended, change_status_to_order_cancelled, change_email_adress_to_empty]



@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['sub_id', 'user']
    readonly_fields = ['sub_id']

@admin.register(OrderResultItem)
class OrderResultItemAdmin(admin.ModelAdmin):
    list_display = ['order_result', 'result_item']



class OrderResultItemInline(admin.TabularInline):
    model = OrderResultItem
    extra = 0



@admin.register(OrderResult)
class OrderResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'survey']
    inlines = [OrderResultItemInline]