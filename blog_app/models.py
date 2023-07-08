from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class post(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = models.TextField()
    creat_date=models.DateField(default=timezone.now)
    published_date=models.DateField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def not_approve_comments(self):
        return self.comments.filter(approved_comment=False)
    
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={"pk":self.pk})
    
    def __str__(self) -> str:
        return self.title
    



class comment(models.Model):
    post=models.ForeignKey("blog_app.post",related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self) -> str:
        return self.text
    
class login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)