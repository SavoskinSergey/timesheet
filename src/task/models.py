from django.db import models
from django.utils import timezone

TODO_STATUS = (
    ('N', 'New'),
    ('S', 'Started'),
    ('F', 'Finished'),
)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    due_date = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    category = models.ForeignKey(Category, default='general', on_delete=models.CASCADE)

    status = models.CharField(max_length=1, choices=TODO_STATUS, default='N')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
