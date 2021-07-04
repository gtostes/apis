from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField()
    amount = models.IntegerField()
    crypto_amounts = models.JSONField()

    def __str__(self):
        return self.user_id