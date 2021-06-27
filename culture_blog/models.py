from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField()
    img_description = models.CharField(max_length=200, blank=True)
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def snip(self):
        return self.text[:30]

    def __str__(self):
        return self.title
