from django.db import models

# Create your models here.
class Documento(models.Model):
    title = models.CharField(max_length=200)
    publication = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    # def getContent() method to get the content of the text