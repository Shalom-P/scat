from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_sentence,name='add-sentence'),
    path('hi',views.get_the_sentence,name='get_the_sentence'),
]