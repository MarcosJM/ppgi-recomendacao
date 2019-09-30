from django.shortcuts import render
from .models import Documento


# Create your views here.
def document_list(request):
    documents = Documento.objects.all().order_by('title')
    return render(request, 'recomendacao/document_list.html', {'documents':documents})