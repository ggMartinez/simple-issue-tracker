from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    STATUS = (
        ('O', 'Open'),
        ('C', 'Closed'),
    )
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=300)
    status = models.CharField(max_length=1, choices=STATUS)
    author = models.CharField(max_length=30)
    asignee = models.ForeignKey(User)
    created_date = models.DateField(auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
