# Create your models here.
import uuid
from django.db import models
from django.conf import settings

class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Column(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE,related_name='columns')
    title = models.CharField(max_length=150)
    order = models.IntegerField(default=0)      #用来排序
    created_at = models.DateTimeField(auto_now_add=True)

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)