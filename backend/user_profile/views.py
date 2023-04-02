from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User_Profile
from django.http import Http404
from rest_framework import status
from .serializers import User_ProfileSerializer
from django.contrib.auth.models import User
from django.db.models import Q

class Register(APIView):
    def put(self, request, format=None):
        user = User.objects.last().id
        data = self.request.data
        user_profile = User_Profile.objects.get(user=user)
        serializer = User_ProfileSerializer(user_profile, data=data, partial = True)
        if serializer.is_valid():
            profile = serializer.save()
            profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class ChangeAvatar(APIView):
    def put(self, request, format=None):
        user = self.request.data.get('id') 
        data = self.request.data
        user_profile = User_Profile.objects.get(user=user)
        serializer = User_ProfileSerializer(user_profile, data=data, partial = True)
        if serializer.is_valid():
            profile = serializer.save()
            if 'image' in data:
                profile.image = data['image']
                profile.thumbnail = ''
            profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class ViewAllProfiles(APIView):
    def get(self, request): #! pobieranie wszystkiego
        profiles = User_Profile.objects.filter(Q(deleted = False))                                       #? ktore nie sa usuniete (deleted=False)
        serializer = User_ProfileSerializer(profiles, many = True)
        data = {}
        data['profiles'] = serializer.data
        return Response(data)

class ViewSingleProfile(APIView):
    def get(self, request, id): 
        user = self.get_object(id)
        print(user, "to jest user z virewsow")
        user_profile = User_Profile.objects.get(id=user.id)
        serializer = User_ProfileSerializer(user_profile)                                      #? ktore nie sa usuniete (deleted=False)
        return Response(serializer.data)
    
    #def delete(self, request, id):
        
        #data = self.request.data
        #id = self.request.data.get('id')  
        #data = {}
        #data['deleted'] = True
        #user = self.get_object(id)
        #print(product.deleted)
        #serializer = User_ProfileSerializer(user, data = data, partial=True ) #! serializer wstawia nowe dane
        #if serializer.is_valid():   
        #   serializer.save()
        #   return Response(serializer.data, status=status.HTTP_200_OK)
        #else:
        #  return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def get_object(self, profile_id):
        try:
            return User_Profile.objects.get(user = profile_id)
        except User_Profile.DoesNotExist:
            raise Http404
        
