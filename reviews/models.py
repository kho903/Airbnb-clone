from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """ Review model Definition """

    review = models.TextField()
    Accuracy = models.IntegerField()
    Communication = models.IntegerField()
    Cleanliness = models.IntegerField()
    Location = models.IntegerField()
    Check_in = models.IntegerField()
    Value = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room}'

    def rating_average(self):
        avg = (
            self.Accuracy +
            self.Communication +
            self.Cleanliness +
            self.Location +
            self.Check_in +
            self.Value
        ) / 6
        return round(avg, 2)
    rating_average.short_description = "Avg."