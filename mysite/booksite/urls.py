from django.urls import path
from .views import add_book ,book_list,delete_book,edit_book,book_byID

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('books/', book_list, name='book_list'),
      path('delete/<int:book_id>/', delete_book, name='delete_book'),
      path('edit/<int:book_id>/', edit_book, name='edit_book'),
        path('detail/book_id=<int:book_id>/',book_byID , name='book_byID'),
]