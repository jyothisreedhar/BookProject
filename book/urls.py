from django.contrib import admin
from django.urls import path
from .views import book_create, book_delete, book_view, book_update

urlpatterns = [
    path("create", book_create, name="create"),
    path("delete/<int:id>", book_delete, name="delete"),
    path("view/<int:id>", book_view, name="view"),
    path("update/<int:id>", book_update, name="update"),


]
