from rest_framework import viewsets
from .models import Board, TODO
from .serializers import BoardSerializer, TODOSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def list(self, request, *args, **kwargs):
        response = super(BoardViewSet, self).list(request, *args, **kwargs)
        for board in response.data:
            board['todo_count'] = len(board.pop('todos'))
        return response


class TODOViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
