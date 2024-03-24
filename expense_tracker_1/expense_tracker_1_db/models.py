from datetime import datetime

from django.db import models


# Create your models here.
class Books(models.Model):
    book_id = models.CharField(max_length=255)
    title = models.CharField(max_length=1000, blank=False)
    subtitle = models.CharField(max_length=1000, null=True)
    authors = models.CharField(max_length=1000, blank=False)
    publisher = models.CharField(max_length=1000, blank=False)
    published_date = models.DateField(models.DateField(default=datetime.strptime('7/10/2019', "%m/%d/%Y")))
    category = models.CharField(max_length=1000, blank=False)
    distribution_expense = models.FloatField(default='', null=True)

    def __str__(self):
        return self.title + " By " + self.authors

    objects = models.Manager()