from django.urls import path
from page import views

app_name='page'

urlpatterns = [
    path('intoroduce/', views.introduce, name='introduce'),
    path('service/', views.service , name ='service')
]
