from django.db import models
from django.contrib.auth.models import User

# Control access and workflow of posts
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
THREAD = (
    (0, 'Army'),
    (1, 'Tech')
)

class Post(models.Model):
    """ Model describing what a post is """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200)
    
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    status = models.IntegerField(choices=STATUS, default=0)
    thread = models.IntegerField(choices=THREAD, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
