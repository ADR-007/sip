from django.db import models
from accounts.models import User


class SipState(models.Model):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    last_state = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.username)

    def __unicode__(self):
        return str(self)
