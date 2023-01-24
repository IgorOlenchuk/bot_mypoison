from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TelegramUserSerializerGet, TelegramUserSerializerPost, OrderSerializerPost, OrderSerializerGet, SettingsSerializerGet
from .models import TelegramUser, Order, Settings


@api_view(['POST'])
def user_post(request):
    serializer = TelegramUserSerializerPost(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_get(request, pk):
    user = get_object_or_404(TelegramUser, pk=user_id)
    serializer = TelegramUserSerializerGet(user)
    return Response(serializer.data)


@api_view(['GET'])
def user_ids_list(request):
    users = TelegramUser.objects.all()
    return Response(data=users.values_list('id', flat=True))


@api_view(['GET'])
def user_respondents_list(request):
    users = TelegramUser.objects.filter(is_respondent=True)
    return Response(data=users.values_list('id', flat=True))


@api_view(['GET'])
def order(request, pk):
    orders = get_object_or_404(Order)
    serializer = OrderSerializerGet(orders)
    return Response(serializer.data)


@api_view(['POST'])
def order_post(request, pk):
    serializer = OrderSerializerPost(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def settings(request, pk):
    settings = get_object_or_404(Settings, pk=pk)
    serializer = SettingsSerializerGet(settings)
    return Response(serializer.data)

