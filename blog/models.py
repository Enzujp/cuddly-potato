from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    intro = models.TextField()
    body= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
        #helps organize posts in time of posting

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email= models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)