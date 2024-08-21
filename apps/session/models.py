from django.db import models

# Register your models here.


class Session(models.Model):

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, to_field='username')
    question= models.ForeignKey('question.Question', on_delete=models.CASCADE)
    correct = models.BooleanField(null=False)
    hint = models.BooleanField(null=False)

    def __str__(self):
        return f"Session {self.user} - {self.correct}"