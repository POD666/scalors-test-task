from __future__ import unicode_literals

from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)


class TODO(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField()

    board = models.ForeignKey(Board)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.title)
