from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.utils.text import slugify
import string
import random


class Profile(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog")
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def generate_random_string(self, N):
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=N))

    def generate_slug(self, text):
        new_slug = slugify(text)
        if BlogModel.objects.filter(slug=new_slug).exists():
            return self.generate_slug(text + self.generate_random_string(5))
        return new_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
