# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import Build


class BuildSerializer(serializers.ModelSerializer):

    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Build
        fields = [
            'pk',
            'url',
            'title',
            'creation_date',
            'completion_date',
            'part',
            'quantity',
            'notes']
