from django.urls import path
import blog.views

app_name = 'blog'
urlpatterns = [
    
    #ex: blog/
    path('', blog.views.home, name = "home"), 
    path('<int:blog_id>', blog.views.detail, name = "detail"), #blog 반복 없애기
    path('<int:blog_id>/comment', blog.views.add_comment_to_post, name='add_comment_to_post'),
    
    #ex: blog/new
    path('new/', blog.views.new, name="new"),
    path('create/', blog.views.create, name="create"),
    path('delete/<int:blog_id>', blog.views.delete, name="delete"),
    path('edit/<int:blog_id>', blog.views.edit, name="edit"),
    path('update/<int:blog_id>', blog.views.update, name="update")

   
]

