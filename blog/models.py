from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return '/%s/' % self.slug

class Post(models.Model):

    ACTIVE = 'active'
    DRAFT = 'draft'
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
        (DELETED, 'Deleted'),
    )


    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE )
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    intro = models.TextField()
    body= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)


    class Meta:
        ordering = ('-created_at',)
        #helps organize posts in time of posting

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email= models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name