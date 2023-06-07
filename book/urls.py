from django.urls import path
from book.views import *

urlpatterns = [
    path('addBook', addBook),
    path('deleteBook', deleteBook),
    path('modifyBook', modifyBook),
    path('BookPopularityAdd', BookPopularityAdd),
    path('modifyScore', modifyScore),
    path('getBookById',getBookById),
    path('getBookByAuthor', getBookByAuthor),
    path('getBookByMainType', getBookByMainType),
    path('getBookByTwoType', getBookByTwoType),
    path('searchBookByKey', searchBookByKey),
    path('getBookSource', getBookSource)

]