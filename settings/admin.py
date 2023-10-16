from django.contrib import admin
from .models import Regulation, Price, ActivityLog

# Register your models here.

@admin.register(Regulation)
class RegulationAdmin(admin.ModelAdmin):
    list_display = ['regulation_id', 'language', 'is_active', 'type_regulations']
    readonly_fields = ["created_at", "updated_at"]
    list_filter = ['language', 'is_active', 'type_regulations', 'created_at', 'updated_at']

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['price_id', 'currency', 'is_active', 'valid_at', 'price']
    readonly_fields = ['created_at']
    list_filter = ['currency', 'is_active', 'valid_at', 'price']


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ['activity_type','created_at', 'user_log', 'text_log', 'status_log']
    readonly_fields = ['activity_id', 'created_at','activity_type', 'user_log', 'text_log', 'status_log']
    list_filter = ['activity_type', 'status_log', 'status_log']
    search_fields = ['user_log', 'activity_id']