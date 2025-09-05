from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book, Author, Member, BorrowRecord
from .serializers import BookSerializer, BookListSerializer, AuthorSerializer, MemberSerializer, BorrowRecordSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated 
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing authors.
    Supports search by name and biography.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','biography']
    def get_permissions(self):
        if self.action in ['create','post','patch','destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]    

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing books.
    Supports filtering by category, author, and availability status.
    Supports search by title, category, and author name.
    """
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category', 'author', 'availability_status']
    search_fields = ['title', 'category', 'author__name']
    
    # @swagger_auto_schema(
    #     operation_summary='List of all books',
    #     operation_description="List all books or search/filter by fields."
    # )
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # @swagger_auto_schema(
    #     operation_summary='Retrive a book',
    #     operation_description="Retrieve a single book by it's ID."
    # )
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # @swagger_auto_schema(
    #     operation_summary= "Create Book",
    #     operation_description="Create a new book."
    # )
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # @swagger_auto_schema(operation_summary='Update a book',operation_description="Update a book.")
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    def get_permissions(self):
        if self.action in ['create','post','patch','destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer


class MemberViewSet(viewsets.ModelViewSet): 
    """
    API endpoint for viewing and editing members.
    Supports search by name and email.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email']
    permission_classes = [IsAdminUser]
    
class BorrowRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing borrow records.
    Supports filtering by status, book, and member.
    """
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['status', 'book','member']
    
    def get_permissions(self):
        if self.action in ['create','post','patch','destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
