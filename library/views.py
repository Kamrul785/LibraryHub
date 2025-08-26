from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book, Author, Member, BorrowRecord
from .serializers import BookSerializer, BookListSerializer, AuthorSerializer, MemberSerializer, BorrowRecordSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','biography']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['category', 'author', 'availability_status']
    search_fields = ['title', 'category', 'author__name']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer


class MemberViewSet(viewsets.ModelViewSet): 
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email']

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['status', 'book','member']
