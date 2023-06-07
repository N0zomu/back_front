from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Note

import json
from django.http import JsonResponse, HttpResponseBadRequest


# 增加一条笔记
@csrf_exempt
def create_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        book_id = data.get('book_id')
        chapter_id = data.get('chapter_id')
        color = data.get('color')
        content = data.get('content')
        range1 = data.get('range1')
        note_text = data.get('note')
        cfi = data.get('cfi')

        note = Note.objects.create(
            user_id=user_id,
            book_id=book_id,
            chapter_id=chapter_id,
            color=color,
            content=content,
            range1=range1,
            note=note_text,
            cfi=cfi
        )
        note.save()
        return JsonResponse({'message': 'Note created successfully.'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

# 查看笔记
@csrf_exempt
def view_all_note(request, user_id, book_id):
    if request.method == 'POST':
        notes = Note.objects.filter(user_id=user_id, book_id=book_id)
        note_data = []
        for note in notes:
            note_data.append({
                'note_id': note.note_id,
                'user_id': note.user_id,
                'book_id': note.book_id,
                'chapter_id': note.chapter_id,
                'color': note.color,
                'content': note.content,
                'range1': note.range1,
                'note': note.note,
                'cfi': note.cfi,
            })
        return JsonResponse({'notes': note_data, 'message': 'Success'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

# 更新笔记color
@csrf_exempt
def update_note_color(request):
    data_json = json.loads(request.body)
    note_range = data_json['range']
    color = data_json['color']
    try:
        note = Note.objects.get(range1=note_range)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Note not found.'}, status=404)
    if request.method == 'POST':
        # note_text = request.POST.get('note')
        # 更新note的字段值
        note.color = color
        note.save()
        return JsonResponse({'message': 'NoteColor updated successfully.'})
    return HttpResponseBadRequest('Invalid request method.')

# 更新笔记text
@csrf_exempt
def update_note_text(request):
    data_json = json.loads(request.body)
    note_range = data_json['range']
    text = data_json.get('text', '')
    try:
        note = Note.objects.get(range1=note_range)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Note not found.'}, status=404)

    if request.method == 'POST':
        note.note = text
        note.save()
        return JsonResponse({'message': 'Note updated successfully.'})
    return HttpResponseBadRequest('Invalid request method.')

# 删除笔记
@csrf_exempt
def delete_note(request):
    data_json = json.loads(request.body)
    note_range = data_json['range']
    note = get_object_or_404(Note, range1=note_range)
    try:
        note = Note.objects.get(range1=note_range)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Note not found.'}, status=404)
    if request.method == 'POST':
        note.delete()
        return JsonResponse({'message': 'Note deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
