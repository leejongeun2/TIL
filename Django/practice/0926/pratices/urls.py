from django.urls import path
from . import views

urlpatterns = [
    path('is-odd-even/<number>/', views.number),
    path('calculate/<a>/<b>', views.num),
    path('name/', views.name),
    path('answer/', views.answer),
    path('lorem_input/', views.lorem_input),
    path('lorem_result/', views.lorem_result),
]