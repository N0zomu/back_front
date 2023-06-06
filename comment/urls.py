from django.urls import path
from comment.views import *

urlpatterns = [
    path('add_comment', add_comment),
    path('search_comment', search_comment),
]