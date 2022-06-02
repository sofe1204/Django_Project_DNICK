from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    files = models.FileField(upload_to=None, max_length=254)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #commentar = models.ForeignKey(Commentar, on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return self.title

class Commentar(models.Model):
    comm_content = models.TextField(null=True, blank=True)
    blog_post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,null=True,blank=True)
    #author = models.ForeignKey(user, on_delete=models.CASCADE, null=True, blank=True)

class BlogPostCommentar(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE, null=True, blank=True)
    commentar = models.ForeignKey(Commentar, on_delete=models.CASCADE, null=True, blank=True)
    blogPost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)




# class BlogPostUser(models.Model):
#     user = models.ForeignKey(user, on_delete=models.CASCADE)
#     blogPost = models.ForeignKey(blogPost, on_delete=models.CASCADE)

