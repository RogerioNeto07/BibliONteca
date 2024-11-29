from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user.urls")),
    path('library/', include("library.urls")),
    path('livro/', include("books.urls")),
]
