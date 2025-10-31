from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import transaction
from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from auctions.models import AuctionItem, Bid
from auctions.serializer import BidCreateSerializer


class CreateBidViewSet(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = BidCreateSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        item_id = serializer.validated_data.get("item_id")
        amount = serializer.validated_data.get("amount")

        with transaction.atomic():
            try:
                item = AuctionItem.objects.select_for_update().get(id=item_id)
            except AuctionItem.DoesNotExist:
                raise serializers.ValidationError("Auction item not found")
            if item.ends_at < timezone.now():
                raise serializers.ValidationError("Auction has already ended")
            if amount <= item.current_price:
                raise serializers.ValidationError(
                    "Bid must be higher than current price"
                )
            item.current_price = amount
            item.save()
            bid = Bid.objects.create(item=item, amount=amount)

        channel_layer = get_channel_layer()
        data = {
            "type": "send_message",
            "message": {
                "text": f"New {bid.id} received",
                "amount": str(amount),
            },
        }
        async_to_sync(channel_layer.group_send)(f"auction_{item_id}", data)
        return Response(BidCreateSerializer(bid).data, status=status.HTTP_201_CREATED)
