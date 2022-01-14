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


COURSES = {}

COURSES["B.TECH"] = {
    "SEMESTERS": [1, 2, 3, 4, 5, 6, 7, 8],
    "BRANCHES": ['CSE', 'IT', 'ECE', 'ME', 'CE']
}
