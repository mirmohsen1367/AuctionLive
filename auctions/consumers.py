import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import AuctionItem

class AuctionsConsumer(AsyncWebsocketConsumer):

  
    @database_sync_to_async
    def check_auction_item(self, room_name):
        try:
            auction_item = AuctionItem.objects.get(id=int(room_name))
            return auction_item
        except (AuctionItem.DoesNotExist, ValueError):
            return None

    async def connect(self):
        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_name = room_name
        self.room_group_name = f"auction_{room_name}"

        auction_item = await self.check_auction_item(room_name)
        if auction_item is None:
            await self.close()
        else:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        await self.close(code=4001)  # Optional: reject sends

    async def send_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps(message, ensure_ascii=False))
