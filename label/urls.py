from django.urls import path
from label.views import *

urlpatterns = [
    path('add_label', add_label),
    path('delete_label', delete_label),
    path('edit_label', edit_label),
    path('search_label', search_label),
]