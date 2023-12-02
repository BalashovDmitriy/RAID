from rest_framework import serializers

from main.models import FrameworkModel


class FrameworkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrameworkModel
        fields = ('pk', 'name')


class FrameworkRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrameworkModel
        fields = ('pk', 'name', 'language')


class FrameworkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrameworkModel
        fields = ('name', 'language')
