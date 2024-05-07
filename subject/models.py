from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Subject(models.Model):
    author = models.CharField(verbose_name='Author', max_length=50)
    title = models.CharField(verbose_name='Title', max_length=50)
    hashtag = models.CharField(verbose_name='Hashtag', max_length=50)
    subject = models.TextField(verbose_name='Subject')
    created_date = models.DateTimeField(verbose_name='Created Date', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Updated Date', auto_now=True)

    def __str__(self) -> str:
        return self.title

    objects = models.Manager()

    class Meta:
        ordering = ['-id']
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class Comment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='comments', verbose_name='Subject')
    commenter = models.ForeignKey(User, on_delete=models.Case, related_name='commenter', verbose_name='Commenter')
    comment = models.TextField(verbose_name='Comment', blank=True, null=True)
    created_date = models.DateTimeField(verbose_name='Created Date', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Updated Date', auto_now=True)
    rating = models.PositiveIntegerField(
        verbose_name='Rating',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self) -> str:
        return str(self.rating)
    
    class Meta:
        ordering = ['-id']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"