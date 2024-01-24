from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.library.models import Book


class BookRateAPIView(APIView):
    def get(self, request, *args, **kwars):
        book_id = self.request.query_params.get("book_id")

        book = Book.objects.get(id=book_id)

        return Response({
            "book_id": book_id, 
            "id": book.id, 
            "name": book.title,
            "rental_fee": book.rental_fee
            }, 
            status=status.HTTP_200_OK)