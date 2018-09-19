from django.urls import path
from . import view
 
urlpatterns = [
    path('search', view.search),
    path('search-form',view.search_form),
    path('',view.login),
]