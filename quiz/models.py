from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct = models.IntegerField()  # 1, 2, 3, 4

    def __str__(self):
        return self.text
