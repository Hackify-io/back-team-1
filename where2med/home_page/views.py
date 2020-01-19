from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from where2med_auth.models import MedicalCenter


# Create your views here.
def index(request):

    return render(request, "home_page/index.html", {})


def list_centers(city, treatment):
    return MedicalCenter.objects.filter(city__icontains=city)
    # medical_centers_by_services = MedicalCenterService.objects.filter(service__icontains=treatment)
    # for medical_centers_by_service in medical_centers_by_services:
    #     if medical_centers.contains()
    # return


class MedicalCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCenter
        fields = ["name", "address", "rate"]


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search(request):
    city = request.query_params.get("city", -1)
    treatment = request.query_params.get("treatment", -1)

    centers = list_centers(city, treatment)
    serializer = MedicalCenterSerializer(centers)

    return Response(serializer.data)


def search_page(request):

    return render(request, "home_page/search.html", {})
