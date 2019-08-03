from django.urls import path
from web import views

app_name = 'web'
urlpatterns = [

    path('sum/<int:first_number>/<int:second_number>', views.sum, name='sum'),
    path('subtraction/<int:first_number>/<int:second_number>', views.subtraction, name='subtraction'),
]
