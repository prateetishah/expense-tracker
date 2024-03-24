from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
from django.core.files.storage import FileSystemStorage
from .models import Books
from tablib import Dataset
from .resources import BookResource
from django.core.exceptions import ValidationError


# Create your views here.

import pandas as pd
from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    # serializer_class = SalesSerializer


@api_view(['GET', 'POST'])
def import_excel_pandas(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        try:
            # Specify engine manually (try 'xlrd' or 'openpyxl')
            empexceldata = pd.read_excel(filename, engine='xlrd')  # Or 'openpyxl' depending on the format

            for row in empexceldata.itertuples():
                # Clean the date string (replace unexpected characters)
                published_date_str = row.published_date.replace("################################################", "")
                try:
                    published_date_obj = pd.to_datetime(published_date_str, format="%m/%d/%Y")  # Adjust format if needed
                    obj = Books.objects.create(
                        book_id=row.id,
                        title=row.title,
                        subtitle=row.subtitle,
                        authors=row.authors,
                        publisher=row.publisher,
                        published_date=published_date_obj,
                        category=row.category,
                        distribution_expense=row.distribution_expense
                    )
                except ValueError:
                    raise ValidationError(f"Invalid date format for row {row.Index}: {row.published_date_str}")

            return render(request, 'expense_tracker_1_db.html', {
                'uploaded_file_url': uploaded_file_url,
                'success_message': 'File imported successfully!'
            })
        except ValidationError as e:
            return render(request, 'expense_tracker_1_db.html', {
                'error_message': str(e)
            })
        except Exception as e:  # Catch other potential errors (optional)
            return render(request, 'expense_tracker_1_db.html', {
                'error_message': f'An error occurred: {str(e)}'
            })

    else:
        return render(request, 'expense_tracker_1_db.html', {})


@api_view(['GET', 'POST'])
def import_excel(request):
    # print("Request Received")
    if request.method == 'POST' :
        Book = BookResource()
        dataset = Dataset()
        new_employee = request.FILES['myfile']
        data_import = dataset.load(new_employee.read())
        result = BookResource.import_data(dataset,dry_run=True)
        if not result.has_errors():
            BookResource.import_data(dataset,dry_run=False)
    return render(request, 'expense_tracker_1_db.html',{})