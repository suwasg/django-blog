from django.db import models
from django.utils.text import slugify
# Create your models here.
# BLOG, CATEGORY-> name, image, description, slug, TAG, COMMENT

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    img = models.FileField(upload_to="category/", null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    img = models.FileField(upload_to="blog/", null=True, blank=True)
    description = models.TextField()
    sort_description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    is_slider = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    tag= models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title 

class Comment(models.Model):
    ratings = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    user = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.CharField(max_length=100, choices=ratings, default=3)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.comment