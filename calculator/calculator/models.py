from django.db import models

class Ans(models.Model):
    answer = models.CharField(max_length=200)
    

    def __str__(self):
        return self.answer