from django.urls import path
from star.views import *

urlpatterns = [
    path('add_star', add_star),
    path('delete_star', delete_star),
    path('list_star', list_star),
]