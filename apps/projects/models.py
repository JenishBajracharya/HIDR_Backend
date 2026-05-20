from django.db import models


class Project(models.Model):

    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile App'),
        ('ai', 'AI/ML'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)

    description = models.TextField()

    image = models.ImageField(upload_to='projects/')

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    date = models.DateField()

    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title