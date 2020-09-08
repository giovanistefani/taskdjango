from django.db import models

# Create your models here.
class Task(models.Model):
    
    STATUS = (
        (1, 'Doing'),
        (2, 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    don = models.CharField(
        max_length=1,
        choices=STATUS,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)