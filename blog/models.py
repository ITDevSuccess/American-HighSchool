from django.db import models
# from django.contrib.auth.models import User
from publication import models as pub_mod

from Web.utils import ImageModel, BaseModel

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(BaseModel, ImageModel):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(pub_mod.Author, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        db_table = "blog"
        verbose_name_plural = "Les Blogs"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Slogan(BaseModel, ImageModel):
    title = models.CharField(max_length=200, unique=True)
    note = models.CharField(max_length=200, null=True)
    description = models.TextField()

    class Meta:
        db_table = "slogan"
        verbose_name_plural = "Les Slogans"

    def __str__(self):
        return self.title
