from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=55, null=True, blank=True)
    surname = models.CharField(max_length=55, null=True, blank=True)
    user_photo = models.ImageField(upload_to="cover_image/", null=True, blank=True)
    interests = models.CharField(max_length=55, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    profession = models.CharField(max_length=55, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            profile = user.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile, sender=User)

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    files = models.FileField(upload_to='blog_files/', null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blocked_user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    # commentar = models.ForeignKey(Commentar, on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return self.title


class Commentar(models.Model):
    comm_content = models.TextField(null=True, blank=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)
    author_com = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class BlogPostCommentar(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE, null=True, blank=True)
    commentar = models.ForeignKey(Commentar, on_delete=models.CASCADE, null=True, blank=True)
    blogPost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)


class Block(models.Model):
    other_user = models.ForeignKey(user, on_delete=models.CASCADE, null=True, related_name='other_user')
    blocked_user = models.ForeignKey(user, on_delete=models.CASCADE, null=True, related_name='blocked_user')
