from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.FileField(upload_to='media/images')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title