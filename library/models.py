from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    isbn = models.CharField(max_length=15, unique=True)
    category = models.CharField(max_length=100)
    availability_status = models.BooleanField(default=True)
    publication_date = models.DateField()
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    membership_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BorrowRecord(models.Model):
    STATUS_CHOICES = [
        ('BORROWED', 'Borrowed'),
        ('RETURNED', 'Returned'),
        ('OVERDUE', 'Overdue'),
    ]
    
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name='borrow_records'
    )
    member = models.ForeignKey(
        Member, 
        on_delete=models.CASCADE,
        related_name='borrow_records'
    )
    borrow_date = models.DateTimeField()
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BORROWED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member.name} - {self.book.title}"

    class Meta:
        ordering = ['-borrow_date']
