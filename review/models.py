from django.db import models

# Create your models here.

# https://www.geeksforgeeks.org/positiveintegerfield-django-models/


class Review(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    stars = models.PositiveIntegerField(choices=(
        (1 , '1 star'), (2 , '2 stars'), (3 , '3 stars'), (4 , '4 stars'), (5 , '5 stars')))
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"
