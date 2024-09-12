from . import views
from django.urls import path

app_name = 'questions-url'

urlpatterns = [
    path('level/<level>/topic/<topic>',views.display_questions_by_level,name='list-questions'),
    path('create/',views.create_question,name='create-questions'),
    path('delete/<id>/',views.delete_question,name='delete-questions')
]  

#<token>
#api/v1/questions/create
#api/v1/questions/delete
