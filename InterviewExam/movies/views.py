from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from .models import Movie
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter


# Removes permissions from views

class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    # queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        """
         Admin: Admin/Staff user can access to all records and can delete also
         User: Normal user can only access to details to of their own records
        """
        if self.request.user.is_staff:
            return Movie.objects.all()
        else:
            return Movie.objects.filter(
                creator=self.request.user.id)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    # queryset = Movie.objects.all()
    # Permission Class added only Authenticated user can retrieve/Delete/update
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
         Admin: Admin/Staff user can access to all records and can delete also
         User: Normal user can only access to details to of their own records
        """
        if self.request.user.is_staff:
            return Movie.objects.all()
        else:
            return Movie.objects.filter(
                creator=self.request.user.id)
