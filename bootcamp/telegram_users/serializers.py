from rest_framework import serializers

from .models import TelegramUser, Order, Settings


class TelegramUserSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = TelegramUser
        fields = ('id', 'tg_name', 'first_name', 'last_name', 'is_banned', 'is_push_maker', 'is_respondent')


class SettingsSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = ('id', 'k_yuany', 'k_comis_1', 'k_comis_2')


class TelegramUserSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = TelegramUser
        fields = ('id', 'tg_name', 'first_name', 'last_name')


class OrderSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('__all__')


class OrderSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('__all__')