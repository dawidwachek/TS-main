from django.contrib import admin

from .models import  Exercise, Questionnaire, Exclussion, Training


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['exercise_id', 'exercise_name']
    readonly_fields = ("exercise_id","created_at")
    fieldsets = [
        ('Data', {
            'fields':('exercise_id', 'exercise_name', 'is_active', 'description', 'created_at', 'exercise_url')
        })
        ]

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['questionnaire_id', 'user_email', 'created_at' ]
    readonly_fields = ("questionnaire_id","created_at", 'updated_at')
    fieldset = [
        ('data', {
            'fields':('questionnaire_id', 'created_at', 'updated_at', 'user_email', 'often_injury', 'step')
        }),
    ]
    search_fields = ['questionnaire_id', 'user_email']
    date_filter = ['created_at']

@admin.register(Exclussion)
class ExclussionAdmin(admin.ModelAdmin):
    list_display = ['exclussion_id', 'exclussion_name']


class ExerciseInLine(admin.TabularInline):
    #pass
    model = Exercise
    fieldsets = [
        ('None',{
            'fields':('training','exercise_id','exercise_name',)
        })
    ]
    extra = 0

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['training_id', 'email_user']
    inlines = [ExerciseInLine,]
    class Meta:
        model = Training



#admin.site.register(Training, TrainingAdmin)
