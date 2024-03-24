from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

from .models import  Books


class BookRegistration(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_id', 'title', 'subtitle', 'authors', 'publisher', 'published_date', 'category', 'distribution_expense']