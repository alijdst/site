from PIL.Image import Image
from PIL import Image
from django.conf import settings
from django.db import models
from django.urls import reverse


class CustomManager(models.Manager):

     def published(self):

         return self.filter(is_publish=True)


class Posts(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='', default='default.jpg', help_text="Post Picture")
    is_publish = models.BooleanField(default=False)
    slug = models.SlugField(default='')

    objects = CustomManager()

    def save(self):
        
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)


    def __str__(self):
        
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-updated', '-created']
        
    def get_absolute_url(self):
        
        return reverse("post_detail", kwargs={"pk": self.pk})

