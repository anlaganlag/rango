from django.urls import path
from rango import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('about/about1/',views.about1,name='about1'),

]
