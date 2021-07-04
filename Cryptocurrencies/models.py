from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=60)
    today_rate_usd = models.FloatField()
    historical_data_30day = models.JSONField()

    def __str__(self):
        return self.name