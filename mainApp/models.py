from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    STATUS = (
        ('O', 'Open'),
        ('C', 'Closed'),
    )
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=300)
    status = models.CharField(
        max_length=1, choices=STATUS, default=STATUS[0][0])
    author = models.ForeignKey(User, related_name='author')
    asignee = models.ForeignKey(User, related_name='asignee')
    created_date = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def get_status(self):
        if self.status == 'O':
            return 'Open'

        if self.status == 'C':
            return 'Closed'

    def __str__(self):
        return (self.title)
