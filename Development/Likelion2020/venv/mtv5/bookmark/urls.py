from django.urls import path

from bookmark.views import BookmarkLV,BookmarkDV

app_name = 'bookmark'
urlpatterns = [
    #class-based views
    path('',BookmarkLV.as_view(), name='index'),
    path('<int:pk>',BookmarkDV.as_view(), name='detail')   
]

