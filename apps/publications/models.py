from django.db import models

# Create your models here.
from django.db import models

class Publicationk(models.Model):

    PUBLICATION_TYPES = [
        ('report', 'Report'),
        ('brief', 'Brief'),
        ('blog', 'Blog'),
    ]

    title = models.CharField(max_length=255)

    type = models.CharField(
        max_length=20,
        choices=PUBLICATION_TYPES
    )

    file = models.FileField(upload_to='publications/')

    description = models.TextField()

    date = models.DateField()

    def __str__(self):
        return self.title