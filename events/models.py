from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=60)
    public = models.BooleanField

    start_time = models.DateTimeField
    end_time = models.DateTimeField

# class EventJoined(models.Model):
#    event = models.ForeignKey('Event')
#    username = models.ForeignKey('User')
#
#    class Meta:
#        constraints = [
#            models.UniqueConstraint(fields=['event', 'username'], name='unique event join')
#        ]
