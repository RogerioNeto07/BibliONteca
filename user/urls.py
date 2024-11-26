from django.urls import path
from user.views import IndexReader, IndexLibrarian, IndexLoggedOut

urlpatterns = [
    path('indexreader', IndexReader),
    path('indexlibrarian', IndexLibrarian),
    path('indexloggedout', IndexLoggedOut),
]
