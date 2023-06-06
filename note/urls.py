from django.urls import path

from note.views import *

urlpatterns = [
    path('create_note', create_note),
    path('view_all_note/<int:user_id>/<int:book_id>', view_all_note),
    path('update_note_color/<int:note_id>/<str:color>', update_note_color),
    path('update_note_text/<int:note_id>/<str:text>', update_note_text),
    path('delete_note/<int:note_id>', delete_note),
]
