from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ContactSerializer
from rest_framework import viewsets
from .models import Contact

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

@api_view
def contact_view(request, slug):
    contact = Contact.objects.get(slug=slug)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return response(serializer.data)

    # try:
    # except Contact.DoesNotExist:
    #     return response()