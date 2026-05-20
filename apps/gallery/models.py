from django.db import models

class Image(models.Model):

    CATEGORY_CHOICES = [
        ('network', 'Network'),
        ('attack', 'Attack'),
        ('system', 'System'),
        ('ui', 'UI'),
        ('other', 'Other'),
    ]

    image = models.ImageField(upload_to='gallery/')

    caption = models.CharField(max_length=255)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    def __str__(self):
        return self.caption