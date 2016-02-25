# coding: utf-8


from .models import Item, BatchWork
from rest_framework import serializers


class BatchWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchWork
        fields = ('name', 'date')

