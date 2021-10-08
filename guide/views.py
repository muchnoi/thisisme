from django.views import generic 
from django.http import FileResponse
from .models import Reference, ReferenceType
#from django.urls import reverse #Used to generate URLs by reversing the URL patterns
#from django.shortcuts import get_object_or_404

class TypeListView(generic.ListView):
  model = ReferenceType

def document_view(request, pk):
  el = Reference.objects.get(id=pk)
  if el.upload:
    return FileResponse(open(str(el.upload), 'rb'))
  else:
    pass
  

