from django import forms
from django.forms import ModelForm
from .models import Book


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookUpdateForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        price=cleaned_data.get("price")

        if price<0:
            msg="invalid price plz provide valid price"
            self.add_error('price',msg)

# class BookCreateForm(forms.Form):
# book_name = forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))
# author = forms.CharField(widget=forms.TextInput(attrs={'class':'author'}))
# price = forms.IntegerField(widget=forms.TextInput(attrs={'class':'price'}))
# pages = forms.IntegerField(widget=forms.TextInput(attrs={'class':'pages'}))
# category=forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))
