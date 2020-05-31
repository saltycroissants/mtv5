from django.db import models
from django.utils import timezone # 추가
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',default = timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    comment_text =  models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    #updated_at = models.DateTimeField() 
    #approved_comment = models.BooleanField(default=False)

    def approve(self):
        #self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_text