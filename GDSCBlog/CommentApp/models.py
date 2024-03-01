from django.db import models
#from BlogApp.models import Post

class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)
    published_date = models.DateTimeField()
    post = models.ForeignKey('BlogApp.Post', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

