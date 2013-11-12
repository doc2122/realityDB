__author__ = 'doc'

from django.db import models
from django.contrib.auth.models import User

class RealityDB(models.Model):
    name = models.CharField(max_length=100)
    users_id_user = models.ForeignKey(User)
    started = models.DateTimeField('year premiered')
    ended = models.DateTimeField('year ended')
    created = models.DateTimeField('date created')

class Changes(models.Model):
    name = models.CharField(max_length=100)
    users_id_user = models.ForeignKey(User)
    started = models.DateTimeField('year premiered')
    ended = models.DateTimeField('year ended')
    modified = models.DateTimeField('date modified')

class Networks(models.Model):
    name = models.CharField(max_length=100)

class Categories(models.Model):
    name = models.CharField(max_length=100)

class RealityDB_has_categories(models.Model):
    realityDB_id_realityDB = models.ForeignKey(RealityDB)
    categories_id_categories = models.ForeignKey(Categories)

class RealityDB_has_networks(models.Model):
    realityDB_id_realityDB = models.ForeignKey(RealityDB)
    networks_id_networks = models.ForeignKey(Networks)

class Changes_has_categories(models.Model):
    changes_id_changes = models.ForeignKey(Changes)
    categories_id_categories = models.ForeignKey(Categories)

class Changes_has_networks(models.Model):
    changes_id_changes = models.ForeignKey(Changes)
    networks_id_networks = models.ForeignKey(Networks)