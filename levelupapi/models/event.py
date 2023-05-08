from django.db import models


class Event(models.Model):
    description = models.CharField(max_length=150)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", related_name="attending")
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="event")

    @property
    def joined(self):
        '''event joined def'''
        return self.__joined

    @joined.setter
    def joined(self, value):
        '''sets the event joined'''
        self.__joined = value
