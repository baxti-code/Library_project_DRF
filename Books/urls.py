from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookViewSet, BookListCreateView, BookDetailUpDelView, BookListAPIView, BookDetailAPIView, BookCreateAPIView
    # BookListAPiView, BookDetailApiView, \
    # BookUpdateApiView, BookDeleteApiView, book_api_view

router = SimpleRouter()
router.register('books', BookViewSet, basename = 'books')

urlpatterns = [
    # path('books/', BookListAPIView.as_view()),
    # path('booklistcreate/', BookListCreateView.as_view()),
    # path('bookdetailupdel/<int:pk>/', BookDetailUpDelView.as_view()),
    # path('books/<int:pk>/', BookDetailAPIView.as_view()),
    # path('bookcreate/', BookCreateAPIView.as_view()),
    # path('<int:pk>/', BookDetailApiView.as_view()),
    # path('<int:pk>/delete/', BookDeleteApiView.as_view()),
    # path('<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/', book_api_view),
]

urlpatterns += router.urls