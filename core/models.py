from django.db import models


class Questionnaire(models.Model):
    questionnaire_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_email = models.EmailField(max_length=100, blank=True)
    weigh = models.DecimalField(max_digits=4, decimal_places=1, default=60)
    injury = models.BooleanField(default=False)
    training = models.BooleanField(default=False)
    often_injury = models.CharField(choices=[
        ("OM", "one on mounth"),
        ("OY", "one on year"),
        ("O5", "one on 5 years"),
        ("NI", "i don't have injury"),
    ], default="NI", max_length=255)
    often_training = models.CharField(choices=[
        ("OM", "one on mounth"),
        ("OY", "one on year"),
        ("O5", "one on 5 years"),
        ("NI", "i don't have training"),
    ], default="NI", max_length=255)
    
    def __int__(self):
        return f'questionnaire id: {self.questionnaire_id}'
    



class Exclussion(models.Model):
    exclussion_id = models.AutoField(primary_key=True)
    exclussion_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url_link = models.CharField(max_length=1000, default=None, blank=True)
    minimum_repeat = models.DecimalField(max_digits=4, decimal_places=0 , default=None, blank=True)
    maximum_repeat = models.DecimalField(max_digits=4, decimal_places=0 , default=None, blank=True)
    minimum_load = models.DecimalField(max_digits=4, decimal_places=0 , default=None, blank=True)
    maximum_load = models.DecimalField(max_digits=4, decimal_places=0 , default=None, blank=True)
    

    #objectives - list


class Training(models.Model):
    training_id = models.AutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    email_user = models.EmailField(blank=True,null=True, default=None)
    email_creator = models.EmailField(blank=True,null=True, default=None)
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    #exercise_choice = models.ManyToManyField(blank=True)

    #exercise_list = models.ManyToManyField(Exercise, default=None, null=True, blank=True)


class Exercise(models.Model):
    training = models.ForeignKey(Training , on_delete=models.CASCADE)
    #training = models.ManyToManyField(Training)
    exercise_id = models.AutoField(primary_key=True)
    exercise_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True, help_text='how do this exercise')
    exercise_alert = models.TextField(blank=True, null=True, help_text='attenion to')
    exercise_url = models.URLField(blank=True, null=True, help_text='link to video')
    created_at = models.DateTimeField(auto_now_add=True)

    #exercise_line = models.ForeignKey(exercise_id, on_delete=models.CASCADE)

    #def __str__(self):
    #    return self.exercise_name
