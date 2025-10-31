from django.core.validators import MinValueValidator
from django.db import models


class AuctionItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    current_price = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        default=100,
        validators=[MinValueValidator(100)],
    )
    ends_at = models.DateTimeField()

    class Meta:
        ordering = ("-current_price",)
        verbose_name = "Auction Item"
        verbose_name_plural = "Auction Items"

    @property
    def winner(self):
        bid = self.bids.order_by("-amount").first()
        if bid:
            return f"winner is bid {bid.id} with amount {bid.amount}"
        return None

    def __str__(self):
        return (
            f"{self.name} - {self.current_price} ends at {self.ends_at:%Y-%m-%d %H:%M})"
        )


class Bid(models.Model):
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(
        max_digits=15, decimal_places=0, validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Bid"
        verbose_name_plural = "Bids"

    def __str__(self):
        return f"{self.item.name} - {self.amount} create at {self.created_at:%Y-%m-%d %H:%M}"
