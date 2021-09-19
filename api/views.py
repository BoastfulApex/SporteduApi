from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Profiles': '/profiles/',
        'Create': '/profile-create/',
        'Update': '/profile-update/<str:pk>/',
        'Delete': '/profiles/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def profileList(request):
    serializer = ProfileSerializer(Profile.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def profileCreate(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def profileUpdate(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def profileDelete(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete(
    )
    return Response(serializer.data)


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            profile = Profile.objects.create(
                full_name=data['full_name'],
                phone=data['phone'],
                Passport=data['Passport'],
                Hudud=data['Hudud'],
                Shahar=data['Shahar'],
                tashkilot=data['tashkilot'],
                malumot=data['malumot'],
                mutaxasislik=data['mutaxasislik'],
                lavozim=data['lavozim'],
                unvoni=data['unvon'],
                oqishshakli=data['oqishshakli'],
                oqishturi=data['oqishturi'],
                sportturi=data['sportturi'],
                talimtili=data['talimtili'],
                passportcopy=data['passportcopy'],
                image=data['image'],
                diplomcopy=data['diplomcopy'],
                inn=data['inn'],
                buyruq=data['buyruq'],
                razryad=data['razryad'],
            )
            profile.save()
            return Response({'status': 'created'}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
