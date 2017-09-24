from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
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

    @detail_route()
    def uncompleted(self, request, *args, **kwargs):
        board = self.get_object()
        uncompleted_todos = board.todos.filter(done=False)
        serializer = TODOSerializer(uncompleted_todos, context={'request': request}, many=True)
        return Response(serializer.data)


class TODOViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
