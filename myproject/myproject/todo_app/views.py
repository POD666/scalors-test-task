from rest_framework import viewsets
from .models import Board
from .serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def list(self, request, *args, **kwargs):
        response = super(BoardViewSet, self).list(request, *args, **kwargs)
        # add todo_count to response here, but later
        return response
