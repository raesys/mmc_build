from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    summary = models.CharField(max_length=200)

    class Meta:verbose_name_plural = 'Series'

    def __str__(self):
        return self.title

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField('date published', default=timezone.now)
    series = models.ForeignKey(Series, default=1, verbose_name='Series', on_delete=models.SET_DEFAULT)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title

