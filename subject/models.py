from django.db import models

# Create your models here.


class Subject(models.Model):
    author = models.CharField(verbose_name='Author', max_length=50)
    title = models.CharField(verbose_name='Title', max_length=50)
    hashtag = models.CharField(verbose_name='Hashtag', max_length=50)
    subject = models.TextField(verbose_name='Subject')
    created_date = models.DateTimeField(verbose_name='Created_Date', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Updated_Date', auto_now=True)

    def __str__(self):
        return self.title

    objects = models.Manager()

    class Meta:
        ordering = ['-id']
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
