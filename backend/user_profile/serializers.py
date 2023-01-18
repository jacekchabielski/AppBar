from rest_framework import serializers
from .models import User_Profile

class User_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = ['id', 'created', 'deleted', 'user', 'first_name', 'last_name', 'slug', 'get_image', 'get_thumbnail', 'role', 'workplace']