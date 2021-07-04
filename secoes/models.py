from django.db import models

class Session(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id