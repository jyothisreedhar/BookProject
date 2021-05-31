from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=120, unique=True)
    author = models.CharField(max_length=120)
    price = models.IntegerField(default=50)
    pages = models.IntegerField()
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.book_name
# create tablebook(Book_name varchar(50))
# ORM==>object relational mapper
# insert into Bookvalues('boookname','author','150','250',"category")
# book1=Book(book_name="story",author="V.T",price=250,pages=550,category="romance")
# book1.save()
# book2=Book(book_name="madhavm",author="madhav",price=250,pages=350,category="fiction")
# book2.save()
# select * from book(sql)===>books=Book.objects.all()(orm)
# update Book set author(sql)='mtvasudevan' where id=1;==>
# we have to fetch that book object
# book=Book.objects.get(id=1)(orm)
# book.delete==>delete a book object
