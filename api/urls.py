from django.urls import path

from api import views

urlpatterns = [
    path('create-account/', views.create_account, name='create-account'),
]
