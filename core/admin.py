from django.contrib import admin

from .models import   Questionnaire, Question, Product, AnswerItem, Answer, SurveyAnswerItem, ResultItem, AnswerGoal, AnswerExclusion





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'tag', 'is_active']
    search_fields = ['tag', 'name']
    list_select_related = True


class AnswerItemInline(admin.TabularInline):
    model = AnswerItem
    extra = 0

@admin.register(AnswerGoal)
class AnswerGoalAdmin(admin.ModelAdmin):
    list_display = ['answer', 'result_item',]



class AnswerGoalInline(admin.TabularInline):
    model = AnswerGoal
    extra = 0

class AnswerExclusionInline(admin.TabularInline):
    model = AnswerExclusion
    extra = 0

@admin.register(ResultItem)
class ResultItemAdmin(admin.ModelAdmin):
    list_display = ['name','slug']

#@admin.register(AnswerItem)
class AnswerItemAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']
    #readonly_fields = ['question', 'answer']

@admin.register(SurveyAnswerItem)
class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'survey', 'answer','answer_value']


#register View with Items line
class SurveyAnswerItemInline(admin.TabularInline):
    model = SurveyAnswerItem
    extra = 0


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    inlines = [AnswerGoalInline, AnswerExclusionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'question_types']
    search_fields = ['name']
    readonly_fields = ['question_id']
    #inlines = [AnswerItemInline, GoalItemInline, ExclusionItemInline]
    inlines = [AnswerItemInline]


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['questionnaire_id', 'slug' ,'user_email', 'created_at', 'product' ]
    readonly_fields = ("questionnaire_id","created_at", 'updated_at')
    #fieldset = [
    #    ('data', {
    #        'fields':('questionnaire_id', 'created_at', 'updated_at', 'user_email', 'often_injury', 'step')
    #    }),
    #]
    search_fields = ['questionnaire_id', 'user_email']
    date_filter = ['created_at']
    inlines = [SurveyAnswerItemInline]




