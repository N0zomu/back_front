from django.urls import path
from author.views import *

urlpatterns = [
    path('add_author', add_author),
    path('delete_author', delete_author),
    path('edit_author', edit_author),
    path('search_author', search_author),
]