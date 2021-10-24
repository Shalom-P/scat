from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_the_sentence,name='gsen'),
    path('as',views.add_sentence,name='add-sentence'),
]