from django.urls import path
from chapter.views import *

urlpatterns = [
    path('add_chapter', add_chapter),
    path('delete_chapter', delete_chapter),
    path('get_chapter', get_chapter),

    # 前一项是URL，后面是绑定的 views 中的函数
    # 当匹配到'register'这个 URL 时
    # 将参数传递进 register 函数进行处理
    # 名字允许不一致，一般写成一样的清晰一些
]