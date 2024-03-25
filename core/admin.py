from django.contrib import admin
from accounts.admin import AdminPermissions

from .models import   Questionnaire, Question, Product, AnswerItem, Answer, SurveyAnswerItem, ResultItem, AnswerGoal, AnswerExclusion, ResultCategory, AnswerResultCategoryItem, SurveyResultCategoryItem, ProductCategory, MixerCategory

#@admin.register(AnswerResultCategoryItem)
class AnswerResultCategoryItemAdmin(admin.ModelAdmin):
    list_display = ('result_category', 'answer', 'len_result')
    list_editable = ['len_result', 'answer']
    search_fields = ['result_category', 'answer']



class AnswerResultCategoryItemInline(admin.TabularInline):
    model = AnswerResultCategoryItem
    extra = 0
    classes = ['collapse']


@admin.register(SurveyResultCategoryItem)
class SurveyResultCategoryItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'survey', 'answer')
    search_fields = ['question']
    #autocomplete_fields = ['question']

class SurveyResultCategoryItemInline(admin.TabularInline):
    model = SurveyResultCategoryItem
    extra = 0
    #autocomplete_fields = ['question']

@admin.register(MixerCategory)
class MixerCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, AdminPermissions):

    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    
    list_display = [ 'name', 'tag', 'is_active','is_visible', 'product_type']
    search_fields = ['tag', 'name']
    list_editable = ['is_active', 'is_visible', 'product_type']
    filter_horizontal = ['mixer_category']
    list_select_related = True

@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display=['id', 'name']
    filter_horizontal = ['products']


class AnswerItemInline(admin.TabularInline):
    model = AnswerItem
    extra = 0

#@admin.register(AnswerGoal)
class AnswerGoalAdmin(admin.ModelAdmin, AdminPermissions):

    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    

    list_display = ['answer', 'result_item',]


#@admin.register(AnswerExclusion)
class AnswerExclusionAdmin(admin.ModelAdmin, AdminPermissions):

    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    

    list_display = ['answer', 'result_item',]

@admin.register(ResultCategory)
class ResultCategoryAdmin(admin.ModelAdmin, AdminPermissions):
    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    
    readonly_fields = ['id']
    list_display = ['id', 'name']
    search_fields = ['name']



class AnswerGoalInline(admin.TabularInline):
    model = AnswerGoal
    extra = 0

class AnswerExclusionInline(admin.TabularInline):
    model = AnswerExclusion
    extra = 0

@admin.register(ResultItem)
class ResultItemAdmin(admin.ModelAdmin, AdminPermissions):
    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    
    list_display = ['name','slug', 'category']
    search_fields = ['name']
    #filter_horizontal = ['category']
    list_filter = ['category']
    readonly_fields = ['slug']
    autocomplete_fields = ['category']

#@admin.register(AnswerItem)
class AnswerItemAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']
    #readonly_fields = ['question', 'answer']

@admin.register(SurveyAnswerItem)
class SurveyAnswerAdmin(admin.ModelAdmin, AdminPermissions):

    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    
    list_display = ['question', 'survey', 'answer','answer_value']


#register View with Items line
class SurveyAnswerItemInline(admin.TabularInline):
    model = SurveyAnswerItem
    extra = 0


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin, AdminPermissions):

    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    
    list_display = ['answer','name','id']
    search_fields = ['answer', 'name', 'id']
    
    readonly_fields = ['id']
    inlines = [AnswerGoalInline, AnswerExclusionInline, AnswerResultCategoryItemInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin, AdminPermissions):

    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    
    list_display = ['name', 'question_type']
    search_fields = ['name']
    readonly_fields = ['question_id']
    list_filter = ['question_type']

    #inlines = [AnswerItemInline, GoalItemInline, ExclusionItemInline]
    inlines = [AnswerItemInline]


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin, AdminPermissions):

    def has_delete_permission(self, request, obj=None):
        return AdminPermissions.has_delete_permission(self=self, request=request)
    def has_add_permission(self, request, obj=None):
        return AdminPermissions.has_add_permission(self=self, request=request, obj=None)
    def has_view_permission(self, request, obj=None):
        return AdminPermissions.has_view_permission(self=self, request=request, obj=None)
    def has_change_permission(self, request, obj=None):
        return AdminPermissions.has_change_permission(self=self, request=request,obj=None)
    
    list_display = ['questionnaire_id', 'slug' ,'user_email', 'created_at', 'product' ]
    readonly_fields = ("questionnaire_id","created_at", 'updated_at', 'slug')
 
    search_fields = ['questionnaire_id', 'user_email']
    date_filter = ['created_at']
    inlines = [SurveyAnswerItemInline, SurveyResultCategoryItemInline]




