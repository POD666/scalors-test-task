from rest_framework import serializers
from .models import Board, TODO


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(queryset=TODO.objects.all(), view_name='todo-detail', many=True)

    class Meta:
        model = Board
        fields = ('url', 'name', 'todos')


class TODOSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TODO
        fields = ('url', 'title', 'done', 'board', 'created_at', 'updated_at')
