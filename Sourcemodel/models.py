from django.db import models
from rest_framework import serializers

class Source(models.Model):
    class Meta:
        db_table = "source"

    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"