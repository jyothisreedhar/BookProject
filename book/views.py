from django.shortcuts import render

# Create your views here.
from .forms import BookCreateForm, BookUpdateForm
from django.shortcuts import render, redirect
from .models import Book


def book_create(request):
    form = BookCreateForm()
    context = {}
    context["form"] = form
    books = Book.objects.all()
    context["books"] = books
    if request.method == "POST":
        form = BookCreateForm(request.POST)
        if form.is_valid():
            # book_name = form.cleaned_data.get("book_name")
            # author = form.cleaned_data.get("author")
            # price = form.cleaned_data.get("price")
            # pages = form.cleaned_data.get("pages")
            # category = form.cleaned_data.get("category")
            #
            form.save()
            print("book object saved")
            return redirect("create")
        else:
            form = BookCreateForm(request.POST)
            context["form"] = form
            return render(request, "book/bookcreate.html", context)

    return render(request, "book/bookcreate.html", context)


def book_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("create")


def book_view(request, id):
    book = Book.objects.get(id=id)
    context = {}
    context["book"] = book
    return render(request, "book/bookview.html", context)


def book_update(request, id):
    book = Book.objects.get(id=id)
    form = BookUpdateForm(instance=book)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = BookUpdateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")

    return render(request, "book/bookupdate.html", context)
