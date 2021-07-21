from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.title} "
