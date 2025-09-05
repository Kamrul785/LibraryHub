from django.contrib import admin
from library.models import Author, Book, Member, BorrowRecord

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(BorrowRecord)
