from django.db import models


class post(models.Model):
    tittle = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.tittle
