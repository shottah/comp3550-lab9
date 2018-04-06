# create Trainer Model which maps one to one to User
#  override __str__ method to display name property
from django.db import models
from django.contrib.auth.models import User

class Trainer(models.Model):
    name = models.CharField(max_length=30)
    users = models.OneToOneField(User)
    num_badges = models.IntegerField()

    def __str__(self):
        return self.name