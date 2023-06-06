from django.shortcuts import render
import json
from comment.models import Comment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        user_id = data_json['user_id']
        book_id = data_json['book_id']
        rate = data_json['rate']
        content = data_json['content']
    
        comment = Comment(user_id=user_id, book_id=book_id, rate=rate, content=content)
        
        comment.save()
        return JsonResponse({'result': 1, 'message': '评论添加成功'})

@csrf_exempt
def search_comment(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        book_id = data_json['book_id']
        comments=Comment.objects.filter(book_id=book_id)
        if comments.exists():
            comment_list=[]
            for comment in comments:
                comment_data={
                    'id' : comment.id,
                    'user_id' : comment.user_id,
                    'book_id' : comment.book_id,
                    'rate' : comment.rate,
                    'content' : comment.content
                }
                comment_list.append(comment_data)
            return JsonResponse({'result': 1, 'message': '查询成功', 'comments': comment_list})
        else:
            return JsonResponse({'result': 0, 'message': '未找到匹配的评论'})