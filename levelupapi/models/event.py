from django.db import models


class Event(models.Model):
    description = models.CharField(max_length=150)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", related_name="attending")
