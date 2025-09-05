from rest_framework import serializers
from .models import Book, Author, Member, BorrowRecord
from django.utils import timezone

class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'books_count']
        
    def get_books_count(self, author:Author):
        return author.books.count()

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField(method_name='get_name')
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'category', 'availability_status', 
                 'publication_date', 'total_copies', 'available_copies', 'author',
                  'author_name']
        
    def get_name(self, book:Book):
        return book.author.name

class BookListSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField(method_name='get_name')
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'category', 'availability_status', 
                 'available_copies', 'author_name']
        
    def get_name(self, book:Book):
        return book.author.name

class MemberSerializer(serializers.ModelSerializer):
    borrowed_books_count = serializers.SerializerMethodField(method_name='get_borrowed_books_count')
    
    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'membership_date', 'status', 'borrowed_books_count']
        
    def get_borrowed_books_count(self, member:Member):
        return member.borrow_records.filter(status='BORROWED').count()

class BorrowRecordSerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField(method_name='get_book_title')
    member_name = serializers.SerializerMethodField(method_name='get_member_name')
    is_overdue = serializers.SerializerMethodField(method_name='get_is_overdue')
    
    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'member', 'book_title', 'member_name',
                 'borrow_date', 'due_date', 'return_date', 'status', 
                 'is_overdue', 'created_at', 'updated_at']
        
    def get_book_title(self, borrow_record:BorrowRecord):
        return borrow_record.book.title
    
    def get_member_name(self, borrow_record:BorrowRecord):
        return borrow_record.member.name
        
    def get_is_overdue(self, borrow_record:BorrowRecord):
        return timezone.now() > borrow_record.due_date and not borrow_record.return_date

