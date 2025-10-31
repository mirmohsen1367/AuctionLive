from rest_framework import serializers

from .models import Bid


class BidCreateSerializer(serializers.ModelSerializer):
    item_id = serializers.IntegerField()

    class Meta:
        model = Bid
        fields = ("amount", "item_id")
