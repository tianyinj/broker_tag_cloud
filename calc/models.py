from django.db import models


class TagCloud(models.Model):
	Index = models.CharField(max_length=8)
	Tag = models.CharField(max_length=255)
	Count = models.IntegerField(default=0)
