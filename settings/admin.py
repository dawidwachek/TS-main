from django.contrib import admin
from .models import Regulation, Price, ActivityLog, QuestionSequence, QuestionItem, Translation


# Register your models here.


#register view for models

@admin.register(Regulation)
class RegulationAdmin(admin.ModelAdmin):
    list_display = ['regulation_id', 'language', 'is_active', 'type_regulations']
    readonly_fields = ["created_at", "updated_at"]
    list_filter = ['language', 'is_active', 'type_regulations', 'created_at', 'updated_at']

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['price_id', 'currency', 'is_active', 'valid_at', 'price', 'price_model']
    readonly_fields = ['created_at']
    list_filter = ['currency', 'is_active', 'valid_at', 'price', 'price_model']


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ['activity_type','created_at', 'user_log', 'text_log', 'status_log']
    readonly_fields = ['activity_id', 'created_at','activity_type', 'user_log', 'text_log', 'status_log']
    list_filter = ['activity_type', 'status_log', 'status_log']
    search_fields = ['user_log', 'activity_id']


#register Items line

@admin.register(QuestionItem)
class QuestionItemAdmin(admin.ModelAdmin):
    readonly_fields = ['sequence']

class QuestionSequenceInline(admin.TabularInline):
    readonly_fields = ('sequence',)
    model = QuestionItem
    extra = 0
    


#register View with Items line

@admin.register(QuestionSequence)
class QuestionSequenceAdmin(admin.ModelAdmin):
    readonly_fields = ['question_sequence_id', 'man']
    inlines = [QuestionSequenceInline]
    
    #inlines = [QuestionSequenceItemInLine]

@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    search_fields = ['tag']
    list_display = ['tag', 'l_en', 'l_pl', 'l_de']

    