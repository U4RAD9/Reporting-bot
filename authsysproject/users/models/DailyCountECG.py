from django.db import models
from .Client import Client
from datetime import datetime

class ECGSetCount(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    TotalProposalbyClient = models.IntegerField(default=0)
    TotalCasesDone = models.IntegerField(default=0)
    date_field = models.DateField(default=datetime.now)

    def __str__(self):
        return str(self.client.name) + " - " + str(self.date_field)
