from django.shortcuts import render
from django.shortcuts import render
import json
from chapter.models import Chapter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def add_chapter(request):
    if request.method == 'POST':
        # 检测 POST 类型的请求

        data_json = json.loads(request.body)
        # 此时 data_json 已经转为了字典类型
        book_id = data_json['book_id']
        chapter_no = data_json['chapter_no']
        chapter_name = data_json['chapter_name']
        chapter_href = data_json['chapter_href']
        # 不确定是否有这个参数，使用get

        # 虽然密码一致性与合法性检测一般是前端判断
        # 但是后端最好也加上，以防万一

        chapter = Chapter(book_id=book_id, chapter_no=chapter_no, chapter_name=chapter_name, chapter_href=chapter_href)
        # id 是自动赋值，不需要指明word
        # post 不赋值会使用默认值0

        chapter.save()
        return JsonResponse({'result': 1, 'message': '章节增添成功!'})
        # 正常结束后需要给一个反馈信息
@csrf_exempt
def delete_chapter(request):
    if request.method != 'POST':
        return JsonResponse({'result':0, 'message':'Error'})
    data_json = json.loads(request.body)
    book_id = data_json['book_id']
    chapter_no = data_json['chapter_no']
    chapter = Chapter.objects.get(book_id=book_id, chapter_no=chapter_no)
    chapter.delete()
    return JsonResponse({'result':1, 'message':r'删除成功'})
# Create your views here.

@csrf_exempt
def get_chapter(request):
    if request.method != 'POST':
        return JsonResponse({'result':0, 'message':'Error'})
    data_json = json.loads(request.body)
    book_id = data_json['book_id']
    posts = [{
        'book_id': x.book_id,
        'chapter_id': x.chapter_id,
        'chapter_no': x.chapter_no,
        'chapter_name': x.chapter_name,
        'chapter_href': x.chapter_href
    } for x in Chapter.objects.order_by('chapter_no').filter(book_id=book_id)]
    return JsonResponse({'result':1, 'message':r'获取成功', 'posts':posts})