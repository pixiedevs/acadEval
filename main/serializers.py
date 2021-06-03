from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Contact
        fields = ["name", "mobile_no", "time"]
