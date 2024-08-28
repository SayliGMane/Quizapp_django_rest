from django.db import models
from datetime import datetime

class Session(models.Model):

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, to_field='username')
    session_questions= models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    is_correct = models.BooleanField(null=False)
    hint = models.BooleanField(null=False)
    session_date = models.DateField(default=datetime.today)
    retry_session = models.BooleanField(default=False)
    session_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Session {self.user} - {self.is_correct}"