from django.urls import path

from note.views import *

urlpatterns = [
    path('create_note', create_note),
    path('view_all_note/<int:user_id>/<int:book_id>', view_all_note),
    path('update_note_color', update_note_color),
    path('update_note_text', update_note_text),
    path('delete_note', delete_note),
]
