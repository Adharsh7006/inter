from os import path
from interview_app import views

urlpatterns = [
    path('', views.index, name='index'),
]