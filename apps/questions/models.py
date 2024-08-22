from django.db import models
from apps.core.constant import LEVEL, TOPIC
from django.contrib.postgres.fields import ArrayField

class Question(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    question = models.TextField(max_length=2000)  # NOT NULL
    select_level = models.CharField(max_length=40, choices=LEVEL, default='1')
    select_topic = models.CharField(max_length=80, choices=TOPIC, default='Basics_1')
    correct_answer = ArrayField(models.CharField(max_length=1000), null=False)
    incorrect_answer = ArrayField(models.CharField(max_length=1000), null=False)
    hint = ArrayField(models.CharField(max_length=1000), null=False)
    score = models.SmallIntegerField(null=False)
    #final backup
   



    def __str__(self) -> str:
        return f'{self.question}'


# from django.db import models
# from apps.core.constant import LEVEL,TOPIC
# from django.contrib.postgres.fields import ArrayField


# # Create your models here.
# class Question(models.Model):
        
#         id = models.CharField(max_length=50, primary_key=True)
#         question= models.TextField (max_length=2000) # need to ask  #NOT NULL
#         select_level = models.CharField(max_length=40, choices=LEVEL, default='1')
#         select_topic = models.CharField (max_length=80, choices=TOPIC, default='Basics_1')
#         correct_answer = ArrayField(models.CharField(max_length=1000), null=False)
#         incorrect_answer = ArrayField(models.CharField(max_length=1000),null=False)
#         hint = ArrayField(models.CharField(max_length=1000), null=False)
#         score = models.SmallIntegerField(null=False)
#         date = 


#         def __str__(self) -> str:
#           return f'{self.question} '
        


        
    
	