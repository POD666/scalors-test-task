from rest_framework import serializers
from .models import Board, TODO


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('__all__')


class TODOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = ('__all__')
