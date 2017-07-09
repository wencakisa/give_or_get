from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Item, Deal


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class DealSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)
    message = serializers.CharField(min_length=5, max_length=1024, required=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Deal
        fields = ('id', 'buyer', 'message', 'status')

    def get_status(self, obj):
        return obj.get_status_display()

    def create(self, validated_data):
        request = self.context.get('request')
        item = self.context.get('item')

        message = validated_data.get('message')

        return Deal.objects.create(buyer=request.user, message=message, item=item)


class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=5, max_length=50, required=True)
    description = serializers.CharField(min_length=5, max_length=1024, required=True)

    phone_number = serializers.CharField(max_length=16, required=False)

    owner = UserSerializer(read_only=True)
    deal_set = DealSerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'phone_number', 'owner', 'added_on', 'deal_set')
